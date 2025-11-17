# bin_to_image.py
import numpy as np
import cv2

# --- Read dimensions ---
with open("dimensions.txt", "r") as dim_file:
    width, height = map(int, dim_file.read().strip().split())

print(f"Loaded dimensions: {width} x {height}")
num_pixels = width * height

# --- Read binary data (AES output, remove all newlines) ---
with open("v5/enc_bin.txt", "r") as f:
    data = f.read().replace("\n", "").replace("\r", "").strip()

# Make sure binary data is divisible properly
if len(data) < num_pixels * 8:
    raise ValueError("Binary file does not have enough bits for the expected pixel count!")

# Convert chunks of 8 bits → pixel
pixels = [int(data[i:i+8], 2) for i in range(0, num_pixels * 8, 8)]

# Reshape to original dimension
arr = np.array(pixels, dtype=np.uint8).reshape((height, width))

# Save image
cv2.imwrite("restoredenc_image.png", arr)
print("Restored image saved as restored_image.png")