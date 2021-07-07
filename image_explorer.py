import cv2
import os
import shutil
import math
#from tensorflow import image
#from tensorflow.keras.preprocessing.image import load_img
#from tensorflow.keras.preprocessing.image import save_img
import cv2

INP_SIZE = (800,200)

INTERPOLATION = "bilinear"
path='/home/franck/tensorflow_rmca/biobois_smartwoodid/scans_avec_trames'
dest_path='/home/franck/tensorflow_rmca/biobois_smartwoodid/scans_avec_trames_rearrange_grey'

#dict_f={}

def analyze_img(ifile, iname):
    global INP_SIZE
    global INTERPOLATION
    print(ifile)
    img = cv2.imread(ifile)
    #print(img.shape)
    elems=iname.split("-")
    #print(elems)
    species=elems[1].strip().replace(" ","_")
    print(species)
    #if not(species in dict_f):
    #    dict_f[species]=[]
    #obj={}
    #obj["path"]=ifile
    #obj["filename"]=iname
    #obj["original_shape"]=img.shape
    #dict_f[species].append(obj)
    cp_path=os.path.join(dest_path, species)
    cp_path_f=os.path.join(cp_path, iname.replace(" ", "_"))
    print(cp_path)
    print(cp_path_f)
    os.makedirs(cp_path, exist_ok=True)
    #tfile=load_img(ifile)
    #tmp_i=image.resize_image_with_pad(tfile, INP_SIZE[0], INP_SIZE[1], INTERPOLATION )
    #save_img(path, tmp_i, scale=True)
    im = cv2.imread(ifile)
    old_size = im.shape[:2]
    print(old_size)
    #ratio = float(INP_SIZE)/max(old_size)
    ratio_width=float(INP_SIZE[0])/old_size[1]  
    ratio_height=float(INP_SIZE[1])/old_size[0]
    ratio=min(ratio_width, ratio_height)
    print(ratio)
    #new_size = tuple([int(x*ratio) for x in old_size])
    new_width=int(math.floor(old_size[1]*ratio))
    new_height=int(math.floor(old_size[0]*ratio))
    im = cv2.resize(im, (new_width, new_height))
    
  
    delta_w   = max(INP_SIZE[0] - new_width,0)
    delta_h = max(INP_SIZE[1] - new_height,0)
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [0, 0, 0]
    im=cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
    value=color)

    cv2.imwrite(cp_path_f, new_im)




if __name__ == "__main__":
    #global dict_f
    for root, dirs, files in os.walk(path):
        for name in files:
            print(dirs)
            if name.endswith((".tif")):
                analyze_img(os.path.join(root, name), name)
   
    #rearrange_files()
            

