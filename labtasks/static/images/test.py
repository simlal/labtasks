import skimage.io
import numpy as np
from pathlib import Path

base_dir = Path(__file__).parent
imgfile = base_dir / "logo_pink.png"

img = skimage.io.imread(imgfile)
tmp_arr = img
print(tmp_arr[tmp_arr > 0][-50:])
# inverted = np.invert(img)

# skimage.io.imsave("logo_inverted.png", tmp_arr)