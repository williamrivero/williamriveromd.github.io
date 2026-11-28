import asyncio, json, subprocess, os
from playwright.async_api import async_playwright
TL=json.load(open('/tmp/cav/timeline.json'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':720})
        await pg.goto('file:///tmp/cav/anim.html'); await pg.evaluate(f"TL={json.dumps(TL)}")
        start=0
        ONLY=[int(a) for a in __import__('sys').argv[1:]]
        for i,sc in enumerate(TL['scenes']):
            if ONLY and i not in ONLY: start+=sc['frames']; continue
            tmp=f'/tmp/cav/scene{i}.tmp.mp4'
            ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r','30',tmp],stdin=subprocess.PIPE)
            for f in range(start,start+sc['frames']):
                await pg.evaluate(f"render({f})")
                ff.stdin.write(await pg.screenshot(type='jpeg',quality=92))
            ff.stdin.close(); assert ff.wait()==0
            os.rename(tmp,f'/tmp/cav/scene{i}.mp4'); start+=sc['frames']; print('scene',i,flush=True)
        await b.close()
asyncio.run(main())
