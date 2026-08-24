import cv2
import sys

command_args = [None, None, None]
for index, command_arg in enumerate(sys.argv[1:]):
    command_args[index] = command_arg

INPUT_FILEPATH = command_args[0] or "drone.png"
OUTPUT_FILEPATH = command_args[1] or "coverage.png"
RADIUS = command_args[2] or 5
# Maximum distance from edge a plant pixel can be. Must be positive odd integer.

image = cv2.imread(INPUT_FILEPATH, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 150, 200)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (RADIUS, RADIUS))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(OUTPUT_FILEPATH, closed)
