"""dip_hw2_dft.py: Starter file to run howework 2"""

#Example Usage: ./dip_hw1_filter -i image -m mask
#Example Usage: python dip_hw1_filter.py -i image -m mask


__author__      = "Pranav Mantini"
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"

import cv2
import sys
from resize import resample as rs
from datetime import datetime


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     fitlering method and writes the output image"""

    #Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-m", "--mask", dest="mask",
                        help="specify name of the mask (ideal, butterworth and gaussian", metavar="MASK")
    parser.add_argument("-c", "--cutoff_f", dest="cutoff_f",
                        help="specify the cutoff frequency", metavar="CUTOFF FREQUENCY")
    parser.add_argument("-o", "--order", dest="order",
                        help="specify the order for butterworth filter", metavar="ORDER")

    args = parser.parse_args()

    #Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    #Check resize scale parametes
    if args.mask is None:
        print("Mask not specified using default (ideal)")
        print("use the -h option to see usage information")
        mask = 'ideal'
    else:
        fx = args.resize_x

    if args.resize_y is None:
        print("Resize scale fy not specified using default (1.5)")
        print("use the -h option to see usage information")
        fy = 1.5
    else:
        fy = args.resize_y


    #Check interpolate method argument
    if args.interpolate is None:
        print("Interpolation method not specified, using default=nearest_neighbor")
        print("use the -h option to see usage information")
        interpolation = "nearest_neighbor"

    else:
        if args.interpolate not in ["nearest_neighbor", "bilinear"]:
            print("Invalid nterpolation method, using default=nearest_neighbor")
            print("use the -h option to see usage information")
            interpolation = "nearest_neighbor"
        else:
            interpolation = args.interpolate


    resample_obj = rs.resample()
    resampled_image = resample_obj.resize(input_image, fx=fx, fy=fy, interpolation=interpolation)

    #Write output file
    outputDir = 'output/resize/'

    output_image_name = outputDir+image_name+interpolation+datetime.now().strftime("%m%d-%H%M%S")+".jpg"    
    cv2.imwrite(output_image_name, resampled_image)


if __name__ == "__main__":
    main()







