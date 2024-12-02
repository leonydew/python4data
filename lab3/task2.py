from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
from argparse import ArgumentParser

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument('img_path')
    plt.figure(1, figsize=(8, 8))
    with Image.open(argumentParser.parse_args().img_path) as image:
        r, g, b = image.split()

        axImage = plt.axes()
        axImage.imshow(image)
        axImage.set_xticks([])
        axImage.set_yticks([])

        hist = plt.axes([axImage.get_position().intervalx[1] + 0.07, axImage.get_position().intervaly[0] + 3 * axImage.get_position().height / 4 + 0.04, 0.4, axImage.get_position().height / 4 - 0.04])
        hist.hist(image.histogram(), bins=1000)
    
    try:
        image = io.imread(argumentParser.parse_args().img_path)
        images = [image[:,:,0], image[:,:,1], image[:,:,2]]
        colors = ['r', 'g', 'b']
        for i, img in enumerate(images):
            hist = plt.axes([axImage.get_position().intervalx[1] + 0.07, axImage.get_position().intervaly[0] + (2 - i) * axImage.get_position().height / 4 + 0.04, 0.4, axImage.get_position().height / 4 - 0.04])
            hist.hist(img.flatten(), bins = 256, color=colors[i])

    except:
        print('Something went wront')
    finally:
        plt.show()
