import rasterio 
import uuid
import numpy as np
import utils
import os
from shutil import rmtree

def getCloudPrediction(filePath):
    id=str(uuid.uuid4())
    # n_rows and n_cols can be calculated from the shape of input image divided by 512
    n_rows=5
    n_cols=5
    out=[]
    path="data"
    # make a dir with unique id as name to save intermediate generated images for each request so that we can delete the dir  of images after prediction
    # os.mkdir(path)
    for i in range(n_rows):
        temp=[]
        for j in range(n_cols):
            crop = (i*512,j*512,512,512 )
            image, meta = utils.tif_to_image(filePath, crop=crop, bands=[10,9,8,7,6,5,4,3,2,1])
            with rasterio.open(f"{path}/test{id}{i}{j}.tif", 'w', **meta) as dst:
                dst.write(image)
            res = utils.infer_image(file_path=f"{path}/test{id}{i}{j}.tif", plot=False)
            temp.append(res)
        out.append(np.hstack(temp))
    return np.vstack(out)