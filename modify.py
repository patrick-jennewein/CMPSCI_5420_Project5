import cv2
import numpy as np


def apply_color_transformation(image, color_value):
    # ensure color is within the valid range
    if color_value < 0.08:
        color_value = 0.1

    # create lookup table for color transformation
    lut = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        new_i = i / 256
        exp = (new_i - 0.5) / color_value
        calculated_value = 256 / (1 + np.exp(exp))
        lut[i] = int(calculated_value)

    # apply the LUT to the red channel
    blue, green, red = cv2.split(image)
    red = cv2.LUT(red, lut)
    new_image = cv2.merge([blue, green, red])

    return new_image

def apply_halo_effect(image, halo_value):
    # ensure halo is within the valid range
    halo_value = min(max(halo_value, 0), 255)

    # create a 3-channel float matrix with 0.75 as default
    halo_matrix = np.full((image.shape[0], image.shape[1], 3),
                          0.75,
                          dtype=np.float32)

    # compute the max radius for the halo effect
    max_radius = min(image.shape[0], image.shape[1]) // 2
    radius = int((halo_value / 255) * max_radius)

    # create white circle in the halo matrix, centered in the image
    center = (image.shape[1] // 2, image.shape[0] // 2)
    cv2.circle(halo_matrix, center, radius, (1.0, 1.0, 1.0), -1)

    # apply blur
    if radius > 0:
        halo_matrix = cv2.blur(halo_matrix, (radius, radius))

    # convert to 32-bit and normalize to [0, 1] range
    image = image.astype(np.float32) / 255.0
    new_image = image * halo_matrix

    # convert back to 8-bit and display
    new_image = np.clip(new_image * 255, 0, 255).astype(np.uint8)

    return new_image

def modify_image(val, image):
    # get trackbar positions
    color_value = cv2.getTrackbarPos('Color', 'Trackbars') / 100
    halo_value = cv2.getTrackbarPos('Halo', 'Trackbars')

    # apply color and halo, based upon trackbar
    color_transformed_image = apply_color_transformation(image, color_value)
    halo_image = apply_halo_effect(color_transformed_image, halo_value)
    final_image = halo_image

    # display both
    cv2.imshow('image', final_image)

    return final_image
