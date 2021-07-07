import os
import shutil
path='/home/franck/tensorflow_rmca/biobois_smartwoodid/scans_avec_trames_rearrange_10'

if __name__ == "__main__": 
    to_delete=[]
    print("TEST")
    for root, dirs, files in os.walk(path):           
        for sub in dirs:
            nb_f=len(os.listdir(os.path.join(root, sub)))
            print(sub)
            print(nb_f)
            if(nb_f==1):
                print("DELETE")
                to_delete.append(os.path.join(root, sub))
    for folder in to_delete:
        shutil.rmtree(folder, ignore_errors=True)
