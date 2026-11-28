import json, wave, numpy as np
fps=30
def load(f):
    w=wave.open(f); sr=w.getframerate(); d=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float); return d,sr
def amps(d,sr,frames,lead=0.5):
    spf=sr/fps; out=[]
    for i in range(frames):
        a=int((i/fps-lead)*sr); b=int(a+spf)
        seg=d[max(a,0):max(b,0)] if b>0 else np.array([])
        out.append(np.sqrt(np.mean(seg**2)) if len(seg) else 0.0)
    return np.array(out)
lines=open('script.txt').read().strip().split('\n'); scenes=[]; amp=[]; chunks=[]
for i,l in enumerate(lines):
    d,sr=load(f's{i+1}.wav'); sp=len(d)/sr; fr=round((0.5+sp+0.8)*fps); r=amps(d,sr,fr)
    amp+=[round(float(v),3) for v in np.clip(r/np.percentile(r[r>0],95),0,1)]
    scenes.append(dict(frames=fr,speech=round(sp,3),lead=0.5,text=l))
    buf=np.zeros(int(round(fr/fps*sr))); s0=int(0.5*sr); buf[s0:s0+len(d)]=d; chunks.append(buf)
json.dump(dict(scenes=scenes,amp=amp,fps=fps),open('timeline.json','w'))
w=wave.open('voice.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(np.concatenate(chunks).astype(np.int16).tobytes()); w.close()
print([s['frames'] for s in scenes], sum(s['frames'] for s in scenes)/fps)
