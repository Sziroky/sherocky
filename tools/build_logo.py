import cairosvg, io, os
from PIL import Image
first,d=open('wordmark_path.txt').read().split('\n',1)
W,H=map(int,first.split())
OUT='/home/ancho/web/sherocky/assets/brand/'
C=dict(red='#C8321B',bright='#E9452B',orange='#EE8E37',cream='#F5F2DC',ink='#0F0C0B')
vw,vh=W/8,H/8
def wordmark(fill='currentColor'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw:.1f} {vh:.1f}" role="img" aria-label="Sherocky">
  <title>Sherocky</title>
  <path fill="{fill}" fill-rule="evenodd" transform="scale(0.125)" d="{d}"/>
</svg>
'''
open(OUT+'sherocky-wordmark.svg','w').write(wordmark())
k=500/448; cx,cy=449.5,436.0
tx=(171-cx)*k+500; ty=(328-cy)*k+500
def badge(flat=False, mono=None):
    if mono:
        fg,bg=mono
        rings=f'''<circle cx="500" cy="500" r="500" fill="{fg}"/>
  <circle cx="500" cy="500" r="{341*k:.1f}" fill="{bg}"/>
  <circle cx="500" cy="500" r="{320.5*k:.1f}" fill="{fg}"/>'''
        txt=bg
    else:
        inner = C['bright'] if flat else 'url(#glow)'
        rings=f'''<circle cx="500" cy="500" r="500" fill="{C['red']}"/>
  <circle cx="500" cy="500" r="{379*k:.1f}" fill="{inner}"/>
  <circle cx="500" cy="500" r="{341*k:.1f}" fill="{C['cream']}"/>
  <circle cx="500" cy="500" r="{320.5*k:.1f}" fill="{C['ink']}"/>'''
        txt=C['cream']
    defs='' if (flat or mono) else f'''<defs>
    <linearGradient id="glow" x1="0.15" y1="0.95" x2="0.6" y2="0.35">
      <stop offset="0" stop-color="{C['orange']}"/>
      <stop offset="0.45" stop-color="{C['bright']}"/>
    </linearGradient>
  </defs>
  '''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" role="img" aria-label="Sherocky">
  <title>Sherocky</title>
  {defs}{rings}
  <path fill="{txt}" fill-rule="evenodd" transform="translate({tx:.2f} {ty:.2f}) scale({k/8:.5f})" d="{d}"/>
</svg>
'''
files={'sherocky-badge':badge(),'sherocky-badge-flat':badge(flat=True),
       'sherocky-badge-mono-dark':badge(mono=(C['ink'],C['cream'])),'sherocky-badge-mono-light':badge(mono=(C['cream'],C['ink']))}
for n,s in files.items(): open(OUT+n+'.svg','w').write(s)
def png(svg,w,h=None): return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=w,output_height=h))).convert('RGBA')
sheet=Image.new('RGB',(2050,560),'#808080')
for i,s in enumerate(files.values()): t=png(s,500,500); sheet.paste(t,(10+i*510,30),t)
sheet.save('prev-badges.png')
rows=[(C['cream'],C['ink']),(C['ink'],C['cream']),(C['cream'],C['red'])]
ims=[]
for fg,bg in rows:
    t=png(wordmark(fg),900); b=Image.new('RGB',t.size,bg); b.paste(t,(0,0),t); ims.append(b)
sh=Image.new('RGB',(900,sum(x.height+10 for x in ims)),'white'); y=0
for x in ims: sh.paste(x,(0,y)); y+=x.height+10
sh.save('prev-wordmark.png')
sm=Image.new('RGB',(420,80),'white')
for i,sz in enumerate([32,48,64]):
    t=png(files['sherocky-badge-flat'],sz,sz); sm.paste(t,(10+i*90,8),t)
t=png(wordmark(C['ink']),120); sm.paste(t,(280,30),t)
sm.save('prev-small.png')
for f in sorted(os.listdir(OUT)): print(f, os.path.getsize(OUT+f))
