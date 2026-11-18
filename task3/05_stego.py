import sys
import os
from PIL import Image, ImageDraw

os.makedirs("data", exist_ok=True)
END = "#####END#####"

def make_cover(path):
    img = Image.new("RGB", (400, 200), color=(30, 60, 110))
    draw = ImageDraw.Draw(img)
    draw.text((20, 90), "CampusShield cover image", fill=(255, 255, 255))
    img.save(path)

def embed(message, cover_path, out_path):
    if not os.path.exists(cover_path):
        make_cover(cover_path)

    img = Image.open(cover_path).convert("RGB")
    bits = "".join(format(ord(c), "08b") for c in message + END)

    pixels = list(img.getdata())
    new_pixels = []
    i = 0
    for r, g, b in pixels:
        rgb = [r, g, b]
        for j in range(3):
            if i < len(bits):
                rgb[j] = (rgb[j] & ~1) | int(bits[i])
                i += 1
        new_pixels.append(tuple(rgb))

    img.putdata(new_pixels)
    img.save(out_path)
    print("message hidden in", out_path)

def extract(path):
    img = Image.open(path).convert("RGB")
    bits = ""
    for r, g, b in img.getdata():
        bits += str(r & 1) + str(g & 1) + str(b & 1)

    text = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        text += chr(int(byte, 2))
        if text.endswith(END):
            return text[:-len(END)]
    return text

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "embed":
        embed(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "extract":
        print(extract(sys.argv[2]))
