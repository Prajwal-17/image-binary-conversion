import cv2
import numpy as np

BIN_PATH = "image.bin"
DIM_PATH = "dimensions.txt"
OUT_IMAGE = "restored_image.png"


def bin_to_image_128bits(bin_path, dim_path, out_image):
    # ---- Read dimensions ----
    with open(dim_path, "r") as f:
        width, height, channels = map(int, f.read().strip().split())

    print(f"Loaded dimensions: {width} x {height}, channels = {channels}")

    bits_per_pixel = channels * 8
    total_pixels = width * height
    total_bits = total_pixels * bits_per_pixel

    # ---- Read binary data (remove newlines) ----
    with open(bin_path, "r") as f:
        data = f.read().replace("\n", "").replace("\r", "").strip()

    print(f"Binary bits available: {len(data)}")

    if len(data) < total_bits:
        raise ValueError(
            f"Not enough binary data! Needed {total_bits} bits but got {len(data)}"
        )

    # ---- Decode pixels ----
    pixels = []

    if channels == 1:
        # Grayscale
        for i in range(0, total_bits, 8):
            val = int(data[i:i+8], 2)
            pixels.append(val)

        arr = np.array(pixels, dtype=np.uint8).reshape((height, width))

    else:
        # Color (BGR or BGRA depending on channel count)
        for i in range(0, total_bits, bits_per_pixel):
            pixel_vals = []
            for ch in range(channels):
                start = i + ch * 8
                end = start + 8
                pixel_vals.append(int(data[start:end], 2))
            pixels.append(pixel_vals)

        arr = np.array(pixels, dtype=np.uint8).reshape((height, width, channels))

    # ---- Save image ----
    cv2.imwrite(out_image, arr)
    print(f"✓ Restored image saved as {out_image}")


# ---- Run directly ----
bin_to_image_128bits(BIN_PATH, DIM_PATH, OUT_IMAGE)
