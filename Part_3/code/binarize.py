
import os
import warnings

import skimage
import skimage.filters
import skimage.io
import skimage.morphology
import argparse


def difference_of_gaussians(img, sigma1, sigma2):
    """
    Difference of Gaussians
    :param img: Image object
    :param sigma1: Sigma for first Gaussian
    :param sigma2: Sigma for second Gaussian
    :return: Image object (Gaussian2 - Gaussian1)
    """
    blur1 = skimage.filters.gaussian(img, sigma1)
    blur2 = skimage.filters.gaussian(img, sigma2)
    return blur2 - blur1


def invert_image(img):
    """
    Inverts an image object
    :param img: Image object
    :return: Inverted image object
    """
    return 1 - img


def apply_threshold(img, threshold):
    return img > threshold


def img_to_binary(img, sigma1, sigma2, threshold):
    if (not sigma1) or (sigma1 <= 0):
        raise ValueError("sigma1 must be a positive number [sigma1={sigma1}]".format(sigma1=sigma1))
    if (not sigma2) or (sigma2 <= 0):
        raise ValueError("sigma2 must be a positive number [sigma2={sigma2}]".format(sigma2=sigma2))
    if (not threshold) or (0.0 >= threshold <= 1.0):
        raise ValueError(
            "threshold must be a number between 0.0 and 1.0 [threshold={threshold}]".format(threshold=threshold))

    edge_image = invert_image(difference_of_gaussians(img, sigma1, sigma2))
    binary_image = apply_threshold(edge_image, threshold)
    return binary_image


def makedirs_for_file(path):
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)


def binary_to_skeleton(binary_image):
    skeleton = invert_image(skimage.morphology.skeletonize(invert_image(binary_image)))
    return skeleton


def write_binary_file(binary_image, outfile):
    makedirs_for_file(outfile)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        skimage.io.imsave(outfile, skimage.img_as_ubyte(binary_image))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--img", type=str, required=True,
                        help="The image to binarize")
    parser.add_argument("--output_path", type=str,
                        help="Output path")

    parser.add_argument("--sigma1", type=int, default=1,
                        help="first sigma for the first gaussian filter")
    parser.add_argument("--sigma2", type=int, default=30,
                        help="second sigma for the second gaussian filter")
    parser.add_argument("--threshold", type=float, default=0.87,
                        help="threshold of the method")

    args = parser.parse_args()
    if args.output_path is None or args.output_path == "None":
        args.output_path = ""

    img = skimage.io.imread(args.img, as_gray=True)
    binary_img = img_to_binary(img, sigma1=args.sigma1, sigma2=args.sigma2, threshold=args.threshold)

    _, extension = os.path.splitext(os.path.basename(args.img))
    bin_file_name = "binarizedImage" + extension

    write_binary_file(binary_img, os.path.join(args.output_path, bin_file_name))
