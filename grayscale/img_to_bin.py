# image_to_bin.py
import numpy as np
import cv2

# Load image in grayscale
img = cv2.imread('assets/scenary.jpg', 0)
if img is None:
    raise FileNotFoundError("Image not found!")

height, width = img.shape
print(f"Image size: {width} x {height}")

# --- Save dimensions in separate file ---
with open("dimensions.txt", "w") as dim_file:
    dim_file.write(f"{width} {height}")
print("Dimensions saved in dimensions.txt")

# --- Convert image to binary ---
with open("image.bin", "w") as f:
    for i in range(height):
        for j in range(width):
            pixel = img[i, j]
            bits = format(pixel, "08b")  # faster
            f.write(bits)
print("Binary saved in image.bin")
