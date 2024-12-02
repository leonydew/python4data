from PIL import Image
from argparse import ArgumentParser


if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("img_path")
    with Image.open(argumentParser.parse_args().img_path) as img:
        redSum, greenSum, blueSum = (sum([img.getpixel((i, j))[k] for i in range(img.size[0]) for j in range(img.size[1])]) for k in range(3))
        if redSum >= greenSum and redSum >= blueSum:
            print("Red")
        elif greenSum >= redSum and greenSum >= blueSum:
            print("Green")
        elif blueSum >= redSum and blueSum >= greenSum:
            print("Blue")
    