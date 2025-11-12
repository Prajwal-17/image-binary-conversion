import numpy as np
import cv2

# Load image in grayscale
img = cv2.imread('assets/image.jpg', 0)

if img is None:
    raise FileNotFoundError("Image not found at path: assets/image.jpg")

# Dynamically get the actual size
height, width = img.shape
z = 0
c = 0

# Use "w" mode to overwrite existing file instead of appending
with open("binary.txt", "w") as f:
    print("opened file")
    for i in range(height):
        for j in range(width):
            a = int(img[i, j])
            bits = [(a >> bit) & 1 for bit in range(7, -1, -1)]  # faster bit extraction
            f.write(''.join(map(str, bits)))
            c += 8
            z += 1
            if z == 16:
                f.write('\n')
                z = 0
    print("completed")