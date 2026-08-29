import cv2
import numpy as np
import sys

command_args = [None, None]
for index, command_arg in enumerate(sys.argv[1:]):
    command_args[index] = command_arg

IMAGE_FILEPATH = command_args[0] or "nir.png"
OUTPUT_FILEPATH = command_args[1] or "bare_land.png"

image = cv2.imread(IMAGE_FILEPATH)
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Take everything that is dark gray
ret, light_gray = cv2.threshold(grayscale, 64, 255, cv2.THRESH_BINARY)
ret, dark_gray = cv2.threshold(grayscale, 32, 255, cv2.THRESH_BINARY)
bare_land = cv2.bitwise_and(dark_gray, cv2.bitwise_not(light_gray))

# Erode to remove just the coasts
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
opened = cv2.morphologyEx(bare_land, cv2.MORPH_OPEN, kernel)

# Use that as mask
red = np.zeros_like(image, dtype = np.uint8)
red[:] = (0, 0, 255)
highlight = cv2.bitwise_and(red, red, mask = opened)
result = 0.5 * highlight + 0.5 * image
cv2.imwrite(OUTPUT_FILEPATH, result)
