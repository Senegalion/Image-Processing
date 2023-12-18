from PIL import Image
import numpy as np
import time


def calculate_summed_area_table(image):
    integral_image = np.cumsum(np.cumsum(image, axis=0, dtype=np.int64), axis=1, dtype=np.int64)
    padded_integral_image = np.pad(integral_image, ((1, 0), (1, 0)), mode='constant')
    return padded_integral_image


def mean_filter(image, mask_size):
    summed_area_table = calculate_summed_area_table(image)
    mask_area = mask_size ** 2
    padded_image = np.pad(image, mask_size // 2, mode='constant')
    filtered_image = np.zeros_like(image, dtype=np.uint8)

    for i in range(image.shape[0] - mask_size + 1):
        for j in range(image.shape[1] - mask_size + 1):
            x1, y1 = i, j
            x2, y2 = i + mask_size - 1, j + mask_size - 1
            window_sum = (
                summed_area_table[x2 + 1, y2 + 1] - summed_area_table[x2 + 1, y1] -
                summed_area_table[x1, y2 + 1] + summed_area_table[x1, y1]
            )
            filtered_image[i, j] = window_sum // mask_area

    return filtered_image


IMAGE_PATH = 'road.jpg'
image = Image.open(IMAGE_PATH).convert('L')
pixels = np.array(image)

# Naive approach
start_time = time.time()
naive_filtered_image = mean_filter(pixels, 71)
naive_execution_time = time.time() - start_time
print("Execution time of naive approach:", naive_execution_time)

# Summed-area table approach
start_time = time.time()
filtered_image = mean_filter(pixels, 71)
execution_time = time.time() - start_time
print("Execution time of summed-area table approach:", execution_time)