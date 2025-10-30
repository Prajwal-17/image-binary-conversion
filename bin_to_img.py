import numpy as np
import cv2

with open("binary.txt", "r") as f:
    h, w = map(int, f.readline().strip().split())
    arr = np.zeros((h, w), dtype=np.uint8)
    i, j = 0, 0
    for line in f:
        line = line.strip()
        if len(line) == 8:
            val = int(line, 2)
            arr[i, j] = val
            j += 1
            if j == w:
                j = 0
                i += 1
                if i == h:
                    break

cv2.imshow("Reconstructed", arr)
cv2.imwrite("reconstructed.png", arr)
cv2.waitkey(0)
cv2.destroyAllWindows()
