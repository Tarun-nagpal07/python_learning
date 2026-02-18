'''Write a script that scans a folder, groups files by extension (.txt, .jpg, .pdf etc.), and moves
each file into a subfolder named after its extension using os and shutil.'''

import os
import shutil
folder = './practice'


for f in os.listdir(folder):
    curr_path = os.path.join(folder,f)

    name,extension = os.path.splitext(f)
    if extension == '':
        continue
    extension = extension[1:]
    new_folder = os.path.join(folder,extension)

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    
    new_path = os.path.join(new_folder,f)
    shutil.move(curr_path,new_path)
    

