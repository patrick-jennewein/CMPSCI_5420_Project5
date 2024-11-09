# Created by Patrick Jennewein
# November 18, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse

def main():
    try:
        # parse command line arguments
        args = parse()

        # read original image and validate
        image = cv2.imread(args['image'])

        if image is None:
            raise Exception(f"\nERROR: Invalid image file. You provided: {args['image']}\n")


        # show original image
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(e)
        return 1

    return 0

if __name__ == '__main__':
    main()
