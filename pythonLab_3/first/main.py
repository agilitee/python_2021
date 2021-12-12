import numpy as np
from PIL import Image

for i in range(1, 4):
    img = Image.open('lunar0' + str(i) + '_raw.jpg')
    data = np.array(img)
    updated_data = (data - data.min()) * int(255/(data - data.min()).max())
    res_img = Image.fromarray(updated_data)
    res_img.save('upd_' + str(i) + '.jpg')
