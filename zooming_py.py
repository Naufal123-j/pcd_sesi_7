# -*- coding: utf-8 -*-
"""zooming.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SMnYrFq87CgkD_JcYvZwZiF39I1ZJn6V
"""

import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPlus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)

    # Buat array kosong untuk citra baru
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    # Scaling with bilinear interpolation
    for y in range(new_height):
        for x in range(new_width):
            # Hitung posisi pada gambar asli
            ori_y = y / factor
            ori_x = x / factor

            # Indeks terdekat di sekitar titik asal
            y1, x1 = int(np.floor(ori_y)), int(np.floor(ori_x))
            y2, x2 = min(y1 + 1, height - 1), min(x1 + 1, width - 1)

            # Berat interpolasi
            wy = ori_y - y1
            wx = ori_x - x1

            # Interpolasi bilinear
            top = (1 - wx) * image[y1, x1] + wx * image[y1, x2]
            bottom = (1 - wx) * image[y2, x1] + wx * image[y2, x2]
            imgZoom[y, x] = (1 - wy) * top + wy * bottom

    return imgZoom

# Membaca gambar
image = img.imread("/content/daun kenikir.jpg")
skala = 2.0

# Memperbesar gambar
imgZoom = zoomPlus(image, skala)

# Menyimpan dan menampilkan hasil
img.imwrite("/content/daun kenikir.jpg", imgZoom)
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Zoomed Image")
plt.imshow(imgZoom)
plt.show()