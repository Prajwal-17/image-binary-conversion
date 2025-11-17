#!/usr/bin/env python3
"""
image_to_bin_color_128bits.py

- Reads a color image (keeps BGR channels from OpenCV)
- Writes dimensions to dimensions.txt as: <width> <height> <channels>
- Writes binary ASCII file (bits '0'/'1') with exactly 128 bits per line to image.bin
  (last line is padded with '0' if needed)
"""

import cv2
import argparse
import os

def image_to_bin_128bits(img_path, out_bits_path="image.txt", out_dim_path="dimensions.txt"):
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Could not open image: {img_path}")

    # If image has alpha channel, keep it (channels may be 4).
    # We'll write whatever channels are present.
    if len(img.shape) == 2:
        # single channel (grayscale) — convert to 3-channel if you absolutely want color,
        # but here we respect original and write channels=1
        height, width = img.shape
        channels = 1
    else:
        height, width, channels = img.shape

    print(f"Image loaded: {img_path} -> width={width}, height={height}, channels={channels}")

    # Save dimensions (width height channels)
    with open(out_dim_path, "w") as d:
        d.write(f"{width} {height} {channels}")
    print(f"Dimensions written to: {out_dim_path}")

    bits_per_line = 128
    buffer = ""

    # Iterate in row-major order: for each pixel, write channels in B,G,R,(A) order
    with open(out_bits_path, "w") as out:
        if channels == 1:
            # single channel
            for i in range(height):
                for j in range(width):
                    val = int(img[i, j])
                    buffer += format(val, "08b")
                    # flush 128-bit chunks
                    while len(buffer) >= bits_per_line:
                        out.write(buffer[:bits_per_line] + "\n")
                        buffer = buffer[bits_per_line:]
        else:
            # multi-channel (BGR or BGRA)
            for i in range(height):
                for j in range(width):
                    pixel = img[i, j]  # e.g. [B,G,R] or [B,G,R,A]
                    # ensure iterable gives ints
                    for ch in range(channels):
                        val = int(pixel[ch])
                        buffer += format(val, "08b")
                    # flush 128-bit chunks
                    while len(buffer) >= bits_per_line:
                        out.write(buffer[:bits_per_line] + "\n")
                        buffer = buffer[bits_per_line:]

        # final leftover: pad to 128 bits with zeros and write if any bits left
        if buffer:
            padded = buffer.ljust(bits_per_line, "0")
            out.write(padded + "\n")
            print(f"Last line padded with {bits_per_line - len(buffer)} zeros.")

    print(f"Binary bits written to: {out_bits_path} (128 bits per line)")

def main():
    p = argparse.ArgumentParser(description="Convert color image to ASCII-bit file with 128-bit rows.")
    p.add_argument("image", help="Input image path")
    p.add_argument("--out-bits", default="image.bin", help="Output bits file (default: image.bin)")
    p.add_argument("--out-dim", default="dimensions.txt", help="Output dimensions file (default: dimensions.txt)")
    args = p.parse_args()

    image_to_bin_128bits(args.image, out_bits_path=args.out_bits, out_dim_path=args.out_dim)

if __name__ == "__main__":
    main()
