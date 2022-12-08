import cv2
import numpy as np
import matplotlib.pyplot as plt

# original image
f = cv2.imread('xyz.jpg', 0)

plt.title('Original Image')
plt.imshow(f, cmap='gray')
plt.axis('off')
plt.show()

# image in frequency domain
F = np.fft.fft2(f)

Fshift = F

M, N = f.shape
H = np.zeros((M, N), dtype=np.float32)
D0 = 50

for u in range(M):
    for v in range(N):
        Fshift[abs(u-int(M/2)), abs(v-int(N/2))] = F[u, v]*(-1)**(u+v)

for u in range(M):
    for v in range(N):
        D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
        if D <= D0:
            H[u, v] = 1
        else:
            H[u, v] = 0


Gshift = Fshift * H

Result = Gshift

for u in range(M):
    for v in range(N):
        Result[abs(u-int(M/2)), abs(v-int(N/2))] = Gshift[u, v]*(-1)**(u+v)


g = np.abs(np.fft.ifft2(Result))
plt.title('Ideal Low Pass')
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()


# Filter: High pass filter
H = 1 - H


# Ideal High Pass Filtering
Gshift = Fshift * H


Result = Gshift

for u in range(M):
    for v in range(N):
        Result[abs(u-int(M/2)), abs(v-int(N/2))] = Gshift[u, v]*(-1)**(u+v)


g = np.abs(np.fft.ifft2(Result))
plt.title('Ideal High Pass')
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()