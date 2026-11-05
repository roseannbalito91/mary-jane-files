from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import glob

root=Path(__file__).resolve().parent.parent
source=next((root/'assets').glob('bookshelf-with-books-*.jpg'))
out=root/'assets'/'mary-jane-logo.png'
S=1024
im=Image.new('RGBA',(S,S),'white')
d=ImageDraw.Draw(im)
d.ellipse((12,12,S-12,S-12),fill='white',outline='#06125d',width=26)
d.ellipse((42,42,S-42,S-42),outline='#43c9fa',width=17)
books=Image.open(source).convert('RGB').resize((820,300),Image.Resampling.LANCZOS)
im.paste(books,(102,205))
d=ImageDraw.Draw(im)
d.rounded_rectangle((102,499,922,516),radius=7,fill='#aa723d')
fonts=glob.glob(str(root/'node_modules'/'@expo-google-fonts'/'sacramento'/'*.ttf'))
fonts+=glob.glob('/usr/share/fonts/truetype/**/*Italic*.ttf',recursive=True)
font=fonts[0]
size=156
while size>36:
 f=ImageFont.truetype(font,size)
 box=d.textbbox((0,0),'Mary Jane Files',font=f,stroke_width=3)
 if box[2]-box[0]<850:break
 size-=2
x=(S-(box[2]-box[0]))//2-box[0]
d.text((x,545),'Mary Jane Files',font=f,fill='#06125d',stroke_width=3,stroke_fill='white')
d.arc((225,690,800,780),0,180,fill='#008bda',width=10)
d.arc((160,850,864,950),0,180,fill='#9ee7ff',width=18)
d.arc((160,875,864,975),0,180,fill='#0d9adf',width=14)
mask=Image.new('L',(S,S),0)
ImageDraw.Draw(mask).ellipse((12,12,S-12,S-12),fill=255)
base=Image.new('RGBA',(S,S),'white')
base.paste(im,(0,0),mask)
base.convert('RGB').save(out,optimize=True)
print('Created',out)
