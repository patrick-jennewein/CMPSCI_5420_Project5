import os
import cv2

def save_incremented_filename(base_filename, image_to_save):
    # create counter for incrementing the file name
    i = 1

    # split name into name and extension
    base_name, ext = os.path.splitext(base_filename)

    # find an available filename with an incremented number
    while True:
        new_filename = f"{base_name}-{i}{ext}"
        if not os.path.exists(new_filename):
            cv2.imwrite(new_filename, image_to_save)
            print(f"\tImage saved as '{new_filename}'.")
            break
        i += 1