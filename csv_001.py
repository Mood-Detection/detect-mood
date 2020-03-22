import sys
import os
import numpy as np
from PIL import Image #PIL ( python image library
import csv # comma seprated value


fileslist = []
#  walk OS libraray ka function h ..walk ka function directory r sub directory k ander files check kry ga
for root, dirs, files in os.walk('C:/Users/infinity/AppData/Local/Programs/Python/Python36/face/', topdown=False):
    # topdown used for searching false s direct wo present working directory p ajae ga .start  searching ni kray ga
    
    for name in files:
        print(name)
        if name.endswith('.png'):
            complete_name = os.path.join(root, name)
            print(complete_name)
            fileslist.append(complete_name)
print(fileslist)


for file in fileslist:
    print(file)
    img_file = Image.open(file)
    img_file.show()
    width, height = img_file.size
    print(width,height)
    format = img_file.format
    print(format)
    mode = img_file.mode
    print(mode)
    img_grey = img_file.convert('L')
    mode=img_grey # convert image into grey scaling
    print(mode)
    img_grey.save('result.png')
    img_grey.show()
    print(img_grey.size[1]) # show height
    print(img_grey.size[0]) # show width
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[0], img_grey.size[1]))  # get array value 
    value = value.flatten() #  convert  and show array in a single row
    print(value)
    with open("test.csv", 'a') as csvfile: # create file  & append ( everytime we run new line will be added in next line)
            writer = csv.writer(csvfile) # write  in the file in csv 
            value=writer.writerow(value) # write value in a single row
            print(value)

    
