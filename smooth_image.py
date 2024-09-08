import PIL.Image as Image
import numpy as np
import cv2

def smooth_image(image: Image, kernel_size: int) -> Image:
    image = image.convert("RGB")
    image = np.array(image)
    kernel = np.ones((kernel_size, kernel_size), np.float32) / kernel_size**2
    #gaussian = cv2.getGaussianKernel(kernel_size, 0)
    image = cv2.filter2D(image, -1, kernel=kernel)
    return Image.fromarray(image)

if __name__ == "__main__":
    image = Image.open("dla_1.png")
    image = smooth_image(image, 4)
    image.show()
    image.save("smoothed_image_dla_1.png")