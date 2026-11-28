import json, wave, numpy as np, sys
t=json.load(open('timeline.json')); fps=30
def load(f):
    w=wave.open(f); sr=w.getframerate(); d=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float); return d,sr
def amps(d,sr,frames,lead=0.5):
    spf=sr/fps; out=[]
    for i in range(frames):
        a=int((i/fps-lead)*sr); b=int(a+spf)
        seg=d[max(a,0):max(b,0)] if b>0 else np.array([])
        out.append(np.sqrt(np.mean(seg**2)) if len(seg) else 0.0)
    return np.array(out)
mode=sys.argv[1]
if mode=='check':
    d,sr=load('s3.wav'); sc=t['scenes'][2]; st=sum(s['frames'] for s in t['scenes'][:2])
    r=amps(d,sr,sc['frames']); old=np.array(t['amp'][st:st+sc['frames']])
    for p in (90,95,98): 
        n=np.clip(r/np.percentile(r[r>0],p),0,1); print(p, np.abs(n-old).mean())
if mode=='build':
    lines=open('script.txt').read().split('\n'); old=t['amp']; newamp=[]; offs=[0]; chunks=[]
    for sc in t['scenes']: offs.append(offs[-1]+sc['frames'])
    for i,sc in enumerate(t['scenes']):
        d,sr=load(f's{i+1}.wav'); fr=sc['frames']
        if i in (0,1):
            sp=len(d)/sr; fr=round((0.5+sp+0.8)*fps); r=amps(d,sr,fr)
            a=[round(float(v),3) for v in np.clip(r/np.percentile(r[r>0],95),0,1)]
            sc.update(frames=fr,speech=round(sp,3),text=lines[i])
        else: a=old[offs[i]:offs[i]+fr]
        newamp+=a
        buf=np.zeros(int(round(fr/fps*sr))); s0=int(0.5*sr); buf[s0:s0+len(d)]=d[:len(buf)-s0]; chunks.append(buf)
    # recompute old offsets properly
    t['amp']=newamp; json.dump(t,open('timeline.json','w'))
    w=wave.open('voice.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(np.concatenate(chunks).astype(np.int16).tobytes()); w.close()
    print([s['frames'] for s in t['scenes']], len(newamp))
