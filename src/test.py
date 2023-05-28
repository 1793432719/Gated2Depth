import matplotlib.image as mpig
import numpy as np
from PIL  import Image
import matplotlib.pyplot as plt

img = Image.open("./src/00038.jpg").convert('RGBA')
a_img = np.asarray(img)
print(a_img)