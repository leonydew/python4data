from PIL import Image
from argparse import ArgumentParser


if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("img_path")
    with Image.open(argumentParser.parse_args().img_path) as img:
        channels = [img] + list(img.split())
        outImg = Image.new("RGB", (4 * img.size[0], img.size[1]), "white")
        for i, image in enumerate(channels):
            outImg.paste(image, (i * img.size[0], 0))
        outImg.show()
    