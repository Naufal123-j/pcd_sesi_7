import numpy as np
import imageio as img 
import matplotlib.pyplot as plt 

# Membaca gambar
path = "C:\\gambar\\bunga.jpg"
image = img.imread(path)

height, width = image.shape[:2]

# Buat array kosong untuk hasil mirroring
mirrored_image = np.zeros_like(image)

# Proses mirroring vertikal dan horizontal secara bersamaan
for y in range(height):
    for x in range(width):
        mirrored_image[y, x] = image[height - 1 - y, width - 1 - x]

# Menampilkan gambar asli dan hasil mirroring
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title("Mirrored Image (Vertical & Horizontal)")
plt.imshow(mirrored_image)

plt.show()
