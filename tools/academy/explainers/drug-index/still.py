import asyncio, json, sys
from playwright.async_api import async_playwright
TL=json.load(open('/tmp/dx/timeline.json'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1280,'height':720}); errs=[]
        pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto('file:///tmp/dx/anim.html'); await pg.evaluate(f"TL={json.dumps(TL)}")
        st=[0]
        for s in TL['scenes']: st.append(st[-1]+s['frames'])
        for a in sys.argv[1:]:
            sc,t=a.split(':'); f=st[int(sc)]+int(float(t)*30)
            await pg.evaluate(f"render({f})"); await pg.screenshot(path=f'/tmp/dx/st_{sc}_{t}.jpg',type='jpeg',quality=85)
        print(errs); await b.close()
asyncio.run(main())
