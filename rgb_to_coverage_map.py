import cv2

IMAGE_FILEPATH = "drone.png"
RADIUS = 5 # Maximum distance from edge a plant pixel can be.
# Must be positive odd integer.

image = cv2.imread(IMAGE_FILEPATH, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 150, 200)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (RADIUS, RADIUS))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("coverage.png", closed)
