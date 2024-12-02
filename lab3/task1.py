from skimage import io
from skimage.color import rgb2gray
from skimage.exposure import equalize_adapthist, adjust_sigmoid
from argparse import ArgumentParser
import numpy as np

class ComplexTransform:
    transforms = []
    def getTransformedImage(self, image):
        for transform in self.transforms:
            image = transform(image)
        return image
    __call__ = getTransformedImage

def argToFunc(arg):
    match arg:
        case "filter1":
            return filter1
        case "filter2":
            return filter2
        case "vertical_flip":
            return verticalFlip
        case "horizontal_flip":
            return horizontalFlip
        case "grey_scale":
            return greyScale
        case "crop":
            return crop

def filter1(image):
    return getRecoverImage(equalize_adapthist(image, kernel_size=20))

def filter2(image):
    return getRecoverImage(adjust_sigmoid(image))

def verticalFlip(image):
    return image[::-1, :]

def horizontalFlip(image):
    return image[:, ::-1]

def greyScale(image):
    return getRecoverImage(rgb2gray(image))

def crop(image):
    return image[image.shape[0] // 4: 3 * image.shape[0] // 4, image.shape[1] // 4: 3 * image.shape[1] // 4]

def getRecoverImage(image):
    return (image * 255).astype(np.uint8) 

if __name__ == "__main__":
    argumentParser = ArgumentParser()
    argumentParser.add_argument('train_path')
    argumentParser.add_argument('-filter1', action='store_true')
    argumentParser.add_argument('-filter2', action='store_true')
    argumentParser.add_argument('-vertical_flip', action='store_true')
    argumentParser.add_argument('-horizontal_flip', action='store_true')
    argumentParser.add_argument('-grey_scale', action='store_true')
    argumentParser.add_argument('-crop', action='store_true')
    argumentParser.add_argument('-complex', nargs='+')
    args = vars(argumentParser.parse_args())
    transforms = []
    for arg in args:
        if arg != "complex" and arg != "train_path" and args[arg]:
            transforms.append(argToFunc(arg))
    complexTransform = ComplexTransform()
    if args["complex"] is not None:
        for arg in args["complex"]:
            complexTransform.transforms.append(argToFunc(arg))
        transforms.append(complexTransform)
    trainPath = args["train_path"]
    for imgType in ["cleaned", "dirty"]:
        imgs = io.imread_collection(f"{trainPath}/{imgType}/*")
        i = 20
        for transform in transforms:
            for img in imgs:
                io.imsave(f"{trainPath}/{imgType}/{i:>04}.jpg", transform(img))
                i += 1
