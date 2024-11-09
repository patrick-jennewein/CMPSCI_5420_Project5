import cv2
import numpy as np


def modify_image(val, image):
    # get trackbar positions
    color_value = cv2.getTrackbarPos('Color', 'Trackbars') / 100
    halo_value = cv2.getTrackbarPos('Halo', 'Trackbars')

    # ensure values are in appropriate ranges as per assignment
    if color_value < 0.08:
        color_value = 0.1
    halo_value = min(max(halo_value, 0), 255)

    # apply effects
    modified_image = image.copy()
    modified_image = cv2.addWeighted(modified_image, color_value, np.zeros_like(modified_image), 0, 0)
    modified_image = cv2.add(modified_image, np.full_like(modified_image, halo_value))

    # display image
    cv2.imshow('image', modified_image)

