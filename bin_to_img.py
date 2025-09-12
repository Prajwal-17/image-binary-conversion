import numpy as np
import cv2

# --- IMPORTANT ---
# You MUST set these to the dimensions of your ORIGINAL image.
IMG_HEIGHT = 322
IMG_WIDTH = 619

# Create an empty numpy array to hold the image pixels
# The dtype 'uint8' is for 8-bit integers (0-255), which is perfect for images.
reconstructed_arr = np.zeros((IMG_HEIGHT, IMG_WIDTH), dtype=np.uint8)

try:
    with open("binary.txt", "r") as f:
        # Read the entire file at once and strip out all newline characters
        binary_string = f.read().replace('\n', '')

    print(f"Read {len(binary_string)} binary digits from file.")

    pixel_index = 0
    # Process the binary string in chunks of 8 characters
    for i in range(0, len(binary_string), 8):
        
        # Get one 8-character chunk (e.g., "01101011")
        byte_string = binary_string[i:i+8]

        # Ensure we have a full 8-character chunk
        if len(byte_string) < 8:
            continue

        # Convert the binary string directly to an integer
        pixel_value = int(byte_string, 2)

        # Calculate the correct row and column to place the pixel
        row = pixel_index // IMG_WIDTH
        col = pixel_index % IMG_WIDTH

        # Stop if we've filled the entire array
        if row >= IMG_HEIGHT:
            break
        
        # Place the pixel value in the array
        reconstructed_arr[row, col] = pixel_value
        pixel_index += 1

    # Save the final numpy array as an image file. This is the crucial step.
    cv2.imwrite("reconstructed_image.png", reconstructed_arr)

    print("\nCompleted! Image saved as 'reconstructed_image.png'.")
    print("Find and click the file in the VS Code explorer to view it.")

except FileNotFoundError:
    print("Error: 'binary.txt' not found. Make sure it's in the same folder as the script.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")