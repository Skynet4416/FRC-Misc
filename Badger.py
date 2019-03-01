from PIL import Image, ImageDraw, ImageFont
from random import randint

#Font is Montserrat

TAG_PATH = "Name-tag-Skynet2.png"
# FONT_PATH = r"C:\Users\Nir\Anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\DejaVuSansMono.ttf"
FONT_PATH = r"C:\Users\Nir\Documents\Git Projects\FRC-Misc\Font\Montserrat-Light.ttf"
with open("Names.txt") as f:
    names = []
    for name in f.readlines():
        names.append(name.split(","))
print(names)

img = Image.open(TAG_PATH)
center = [s // 2 for s in img.size]
position = (1000, 100)
print(img.size)

# size = randint(250, 450)
font = ImageFont.truetype(FONT_PATH, size=286)
# print(size)

for name in names:
    draw = ImageDraw.Draw(img)
    size = draw.textsize(name[0], font=font)
    pos = []
    pos.append(center[0] - size[0] // 2 + 50)
    pos.append(center[1] - size[1] // 2  + 55)
    # pos = [c - (p // 2) for c, p in zip(center, size)]
    draw.text(pos, name[0], "orange", font=font)
    draw.text((600, 100), name[1], (36, 36, 51))  # , font=font)
    img.save("{}.png".format(name[0]))