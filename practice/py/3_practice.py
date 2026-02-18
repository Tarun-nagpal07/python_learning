'''Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 
1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png'''

import os

folder = './practice'
ls = os.listdir(folder)


# print(ls)

for i,l in enumerate(ls):
    old = os.path.join(folder,l)
    new  = f"{i}_practice.py"
    new_path = os.path.join(folder,new)

    os.rename(old,new_path)