# fix: image size is fixed to square type

import numpy as np
import cv2

# Read the binary file
with open("binary.txt", "r") as f:
    data = f.read().replace("\n", "").strip()

print(f"Read {len(data)} bits from file.")

# Each pixel is 8 bits
num_pixels = len(data) // 8

# Dynamically decide the image size (assuming square)
side = int(np.sqrt(num_pixels))
print(f"Detected image size: {side}x{side}")

# Convert every 8 bits → 1 pixel
pixels = [int(data[i:i+8], 2) for i in range(0, len(data), 8)]

# Create numpy array and reshape
arr = np.array(pixels[: side * side], dtype=np.uint8).reshape((side, side))

# Save the image (no GUI)
cv2.imwrite("decoded_image.png", arr)
print("✅ Image saved as decoded_image.png")