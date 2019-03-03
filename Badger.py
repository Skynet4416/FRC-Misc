from PIL import Image, ImageDraw, ImageFont

# Font is Montserrat

TAG_PATH = "MINI_TEMPLATE.png"
FONT_PATH = r".\Font\Montserrat-Light.ttf"
FONT_PATH2 = r".\Font\Montserrat-Light.ttf"
MIN_NAME_SIZE = 175  # 1400
MIN_ROLE_SIZE = 75  # 650
LOW_NAME_Y = 110  # 800
LOW_ROLE_Y = 30  # 270
LEFT_SIDE_X = 160  # 1240
ROCKET_RIGHT_X = 57  # 440
CORRECTION_X = 5  # 30
MAX_NAME_FONT = 40  # 286
MAX_ROLE_FONT = 20  # 150
FONT_JUMPS = 1  # 3

with open("Names.txt") as f:
    names = []
    for name in f.read().split("\n"):
        names.append(name.split("--"))
print(names)

original = Image.open(TAG_PATH)
original_size = (original.size[0], LOW_NAME_Y)
center = [s // 2 for s in original_size]
side_center = (original_size[0] + LEFT_SIDE_X) // 2
print(original.size)
print(side_center)

name_fonts = dict()
role_fonts = dict()
name_fonts[MAX_NAME_FONT] = ImageFont.truetype(FONT_PATH, size=MAX_NAME_FONT)
role_fonts[MAX_ROLE_FONT] = ImageFont.truetype(FONT_PATH2, size=MAX_ROLE_FONT)


name_centery = (original_size[1] + LOW_ROLE_Y) // 2
for i, name in enumerate(names):
    i += 23
    img = original.copy()
    draw = ImageDraw.Draw(img)
    font_size = MAX_NAME_FONT
    center[0] = (original_size[0] + ROCKET_RIGHT_X) // 2
    size = [original_size[0]]
    while size[0] > MIN_NAME_SIZE:
        font = name_fonts.get(font_size, None)
        if font is None:
            font = ImageFont.truetype(FONT_PATH, size=font_size)
            name_fonts[font_size] = font
        size = draw.textsize(name[0], font=font)
        font_size -= FONT_JUMPS

    pos = []
    pos.append(center[0] - size[0] // 2)
    pos.append(name_centery - size[1] // 2)
    print(name[0], pos)
    draw.text(pos, name[0], "white", font=font)

    font_size = MAX_ROLE_FONT
    size = [original_size[0]]
    while size[0] > MIN_ROLE_SIZE:
        font = role_fonts.get(font_size, None)
        if font is None:
            font = ImageFont.truetype(FONT_PATH2, size=font_size)
            role_fonts[font_size] = font
        size = draw.textsize(name[1], font=font)
        font_size -= FONT_JUMPS
    pos = []
    pos.append(side_center - size[0] // 2 - CORRECTION_X)
    pos.append(LOW_ROLE_Y // 2 - size[1] // 2)
    print(name[1], pos)
    draw.text(pos, name[1], (36, 36, 51), font=font)
    img.save("Tags\\{}-{}.png".format(i, name[0].strip(".")))

print("Done")
