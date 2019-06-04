from PIL import Image
import numpy as np

# Fuction for rendering output image
def draw_image(arr, output):
    normalized_arr = (arr*255.0/np.amax(arr)).astype(np.uint8)
    im = Image.fromarray(normalized_arr)
    im.save(output, mode="L")