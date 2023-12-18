from PIL import Image

ADDRESS_IMAGE = 'yoda.jpeg'
image = Image.open(ADDRESS_IMAGE)

image_gray = image.convert('L')

# Single Thresholding
THRESHOLD = 128
image_bw_single = image_gray.point(lambda x: 0 if x < THRESHOLD else 255, '1')
image_bw_single.save('yoda_single_thresholding.jpeg')

# Double Thresholding
LOWER_THRESHOLD = 100
UPPER_THRESHOLD = 200
image_bw_double = image_gray.point(lambda x: 0 if x < LOWER_THRESHOLD or x > UPPER_THRESHOLD else 255, '1')
image_bw_double.save('yoda_double_thresholding.jpeg')
