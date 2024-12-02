from pathlib import Path
from PIL import Image
from argparse import ArgumentParser


if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument("-ftype")
    extension = argumentParser.parse_args().ftype
    imgFiles = Path(".").glob(f"*.{extension}")
    for file in imgFiles:
        with Image.open(file.name) as img:
            img.resize((50, 50)).show()
    