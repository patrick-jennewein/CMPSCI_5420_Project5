# Created by Patrick Jennewein
# November 18, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from functools import partial
from modify import modify_image


def main():
    try:
        # parse command line for image and validate
        args = parse()
        image = cv2.imread(args['image'])
        if image is None:
            raise Exception(f"\nERROR: Invalid image file. You provided: {args['image']}\n")

        # create two windows: one for the image, and one for the trackbars
        cv2.namedWindow('image')
        cv2.namedWindow('Trackbars')
        cv2.createTrackbar('Color',
                           'Trackbars',
                           10,  # will be divided by 100 in modify_image()
                           20,  # will be divided by 100 in modify_image()
                           partial(modify_image, image=image))
        cv2.createTrackbar('Halo',
                           'Trackbars',
                           100,
                           200,
                           partial(modify_image, image=image))

        # Display default image
        modify_image(0, image)

        # Wait for user to close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(e)
        return 1

    return 0


if __name__ == '__main__':
    main()
