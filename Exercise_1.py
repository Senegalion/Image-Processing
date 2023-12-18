from PIL import Image

ADDRESS_IMAGE = 'yoda.jpeg'
IMAGE = Image.open(ADDRESS_IMAGE)

if IMAGE.mode != 'RGB':
    IMAGE = IMAGE.convert('RGB')

WIDTH, HEIGHT = IMAGE.size

pixel_values = list(IMAGE.getdata())

pixels = [pixel_values[i:i+WIDTH] for i in range(0, len(pixel_values), WIDTH)]


for row in pixels:
    for R, G, B in row:
        print(f"R: {R}, G: {G}, B: {B}")

IMAGE.close()
