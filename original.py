from operator import xor
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def img2gray(img):

  sliced = img[...,0:3]
  gray = np.dot(sliced, [0.299, 0.587, 0.114])

  return gray
  
if __name__ == "__main__":

  imagebin = Image.open(r'img.png')
  image = np.asarray(imagebin)

  gray_image = img2gray(image)
  print(repr(image))
  plt.imshow(gray_image,cmap="gray")  
  plt.show()

