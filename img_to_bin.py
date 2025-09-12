import numpy as np
import cv2

# Try to read the image in grayscale mode (the '0')
img = cv2.imread('virat.jpg', 0)

# --- IMPORTANT ---
# Check if the image was loaded successfully. If not, print an error.
if img is None:
    print("Error: Could not read image. Make sure 'virat.jpg' is in the same folder as your script.")
else:
    # --- FIX ---
    # Get the height and width from the image itself instead of hardcoding
    h, w = img.shape
    
    z = 0
    c = 0

    # Use 'w' to write a new file each time. 'a' appends to the old one.
    f = open("binary.txt", "w") 
    print("Opened file and starting conversion...")

    for i in range(h):
        for j in range(w):
            a = img[i][j]
            l = []
            # This loop correctly converts the 8-bit pixel value to binary
            for k in range(8):
                b = a % 2
                l.append(b)
                a = a // 2
            
            for ele in reversed(l):
                f.write(str(ele))
                c = c + 1
            z = z + 1
            
            # Adds a newline every 16 pixels processed
            if z == 16:
                f.write('\n')
                z = 0

    f.close() # Always close the file when you're done
    print("Completed. Check for the 'binary.txt' file.")