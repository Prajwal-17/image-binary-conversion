import numpy as np
import cv2

img = cv2.imread("image.jpg", 0)
h, w = img.shape

with open("binary.txt", "w") as f:
  f.write(f"{h} {w}\n")
  for i in range(h):
    for j in range(w):
      a = img[i, j]
      bits = f"{a:08b}"
      f.write(bits + "\n")
print("Binary file created with image size info.")