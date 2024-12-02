from PIL import Image, ImageDraw, ImageFont
     

if __name__ == "__main__":
    img = Image.new("RGB", (100, 100), "black")
    draw = ImageDraw.Draw(img)
    draw.line([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)], width=5, fill=(0, 0, 255))
    font = ImageFont.load_default(size=30)
    for i in range(1, 4):
        numImg = img.copy()
        numDraw = ImageDraw.Draw(numImg)
        numDraw.text((43, 30), str(i), fill=(255, 0, 0), font=font)
        numImg.show()
        numImg.save(f"{i}.png", format="png")
