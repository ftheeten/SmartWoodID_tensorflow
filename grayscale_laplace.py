#python 3.7.4,opencv4.1
#  https://blog.csdn.net/caimouse/article/details/51749579
#
import cv2
import numpy as np
import os
from scipy import signal
 

path='/home/franck/tensorflow_rmca/biobois_smartwoodid/scans_originaux'
dest_path='/home/franck/tensorflow_rmca/biobois_smartwoodid/marr_hildreth'

def edgesMarrHildreth(img, sigma):
 
    """
            finds the edges using MarrHildreth edge detection method...
            :param im : input image
            :param sigma : sigma is the std-deviation and refers to the spread of gaussian
            :return:
            a binary edge image...
    """
    print("A")
    size = int(2*(np.ceil(3*sigma))+1)
 
 
 
    x, y = np.meshgrid(np.arange(-size/2+1, size/2+1),
 
                       np.arange(-size/2+1, size/2+1))
 
 
    normal = 1 / (2.0 * np.pi * sigma**2)
    kernel = ((x**2 + y**2 - (2.0*sigma**2)) / sigma**4) * \
        np.exp(-(x**2+y**2) / (2.0*sigma**2)) / normal  # LoG filter
 
    print("B")
    kern_size = kernel.shape[0]
    log = np.zeros_like(img, dtype=float)
    print("C")
    
    # applying filter
    for i in range(img.shape[0]-(kern_size-1)):
        for j in range(img.shape[1]-(kern_size-1)):
            window = img[i:i+kern_size, j:j+kern_size] * kernel
            log[i, j] = np.sum(window)
  
    print("D")
 
    log = log.astype(np.int64, copy=False)
    zero_crossing = np.zeros_like(log)
         # Calculate 0 cross
    for i in range(log.shape[0]-(kern_size-1)):
        for j in range(log.shape[1]-(kern_size-1)):
            if log[i][j] == 0:
 
                if (log[i][j-1] < 0 and log[i][j+1] > 0) or (log[i][j-1] < 0 and log[i][j+1] < 0) or (log[i-1][j] < 0 and log[i+1][j] > 0) or (log[i-1][j] > 0 and log[i+1][j] < 0):
 
                    zero_crossing[i][j] = 255
 
            if log[i][j] < 0:
 
                if (log[i][j-1] > 0) or (log[i][j+1] > 0) or (log[i-1][j] > 0) or (log[i+1][j] > 0):
 
                    zero_crossing[i][j] = 255
    print("E")
    return zero_crossing
 
if __name__ == "__main__":
    #global dict_f
    for root, dirs, files in os.walk(path):
        for name in files:
            print(dirs)
            if name.endswith((".tif")):
                print(name)
                elems=name.split("-")
                species=elems[1].strip().replace(" ","_")
                cp_path=os.path.join(dest_path, species)
                cp_path_f=os.path.join(cp_path, name.replace(" ", "_"))
                print(cp_path)
                print(cp_path_f)
                os.makedirs(cp_path, exist_ok=True)
                image = cv2.imread(os.path.join(root, name), cv2.IMREAD_GRAYSCALE)
                MH = edgesMarrHildreth(image, 3)
                MH = MH.astype(np.uint8)
                #cv2.imshow("MH",MH)
                cv2.imwrite(cp_path_f, MH)
