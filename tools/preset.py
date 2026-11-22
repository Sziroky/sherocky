"""Preset Sherocky v0: ciepło, przyciemnione cienie, lekko zgaszony kolor. Użycie: python preset.py OUT_DIR nazwa=ścieżka ..."""
import sys
from PIL import Image, ImageOps, ImageEnhance
import numpy as np
def grade(im):
    a=np.asarray(im).astype(np.float32)/255
    a=np.clip((a-0.03)/0.97,0,1)            # przyciemnione czernie
    a=a**1.08                                # lekko głębsze cienie
    lum=a.mean(2,keepdims=True)
    a=lum+(a-lum)*0.88                       # mniej nasycenia (flesz)
    warm=np.array([1.04,1.0,0.90])           # ciepła tonacja
    a=np.clip(a*warm,0,1)
    h,w,_=a.shape; y,x=np.ogrid[:h,:w]
    v=1-0.28*(((x-w/2)/(w/2))**2+((y-h/2)/(h/2))**2)/2  # winieta
    a=a*np.clip(v,0,1)[...,None]
    return Image.fromarray((a*255).astype(np.uint8))
out=sys.argv[1]
for arg in sys.argv[2:]:
    name,path=arg.split('=',1)
    im=ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    im.thumbnail((2400,2400),Image.LANCZOS)
    grade(im).save(f'{out}/{name}.jpg',quality=88)
    print(name, im.size)
