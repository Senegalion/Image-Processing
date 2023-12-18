from PIL import Image
import numpy

image = Image.open('yoda.jpeg').convert('L')

histogram, _ = numpy.histogram(image, bins=256, range=[0, 256])

cdf = histogram.cumsum()

cdf_normalized = cdf * histogram.max() / cdf.max()

equalized_image = numpy.interp(image, range(256), cdf_normalized).astype(numpy.uint8)

Image.fromarray(equalized_image).show()