from operator import xor
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def projectRGB(rgb):
  "takes rgb sequence ( r, g, b) and create projection with boildown function"
  "boildown rule: R2R1R0G1G0B2B1B0 xor R5R4R3G4G3G2B4B3"

  r = rgb[0]
  g = rgb[1]
  b = rgb[2]

  r0 = bit(r, 0)
  r1 = bit(r, 1)
  r2 = bit(r, 2)
  r3 = bit(r, 3)
  r4 = bit(r, 4)
  r5 = bit(r, 5)

  g0 = bit(g, 0)
  g1 = bit(g, 1)
  g2 = bit(g, 2)
  g3 = bit(g, 3)
  g4 = bit(g, 4)

  b0 = bit(b, 0)
  b1 = bit(b, 1)
  b2 = bit(b, 2)
  b3 = bit(b, 3)
  b4 = bit(b, 4)

  # "R2R1R0G1G0B2B1B0"
  left = (r2 << 7) + (r1 << 6) + (r0 << 5) + (g1 << 4) + (g0 << 3) + (b2 << 2) + (b1 << 1) + b0
  # "R5R4R3G4G3G2B4B3"
  right = (r5 << 7) + (r4 << 6) + (r3 << 5) + (g4 << 4) + (g3 << 3) + (g2 << 2) + (b4 << 1)+ b3
  return xor(left, right)

def bit(i, n):
  "returns n'th bit of i"
  return (i >> n) & 1

  
if __name__ == "__main__":

  imagebin = Image.open(r'img.png')
  image = np.asarray(imagebin)

  gray_image = np.apply_along_axis(projectRGB, 2, image)

  plt.imshow(gray_image,cmap="gray")  
  plt.show()

