# Created by Patrick Jennewein
# November 18, 2024
# CS5420, University of Missouri - St. Louis

import cv2
from parse_args import parse
from modify import modify_image
from file_saver import save_incremented_filename


def main():
    try:
        # parse command line for image and validate
        args = parse()
        image = cv2.imread(args['image'])
        if image is None:
            raise Exception(f"\nERROR: Invalid image file. You provided: {args['image']}\n")

        # create two windows
        cv2.namedWindow('image')
        cv2.namedWindow('Trackbars')

        # set default trackbar values and callback function to respond dynamically
        cv2.createTrackbar('Color',
                           'Trackbars',
                           10,  # will be divided by 100 in modify_image()
                           20,  # will be divided by 100 in modify_image()
                           lambda x: modify_image(x, image))  # callback when user slides trackbars
        cv2.createTrackbar('Halo',
                           'Trackbars',
                           100,
                           200,
                           lambda x: modify_image(x, image))  # callback when user slides trackbars
        new_image = modify_image(0, image)

        while True:
            key = cv2.waitKey(1) & 0xFF

            # If the user presses 's', save the current modified image
            if key == ord('s'):
                save_incremented_filename(args['image'], new_image)

            # If the user presses 'q', break the loop and close
            elif key == ord('q'):
                break

            # Update the modified image in case the trackbars were changed
            new_image = modify_image(0, image)

        # terminate program
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(e)
        return 1

    return 0


if __name__ == '__main__':
    main()
