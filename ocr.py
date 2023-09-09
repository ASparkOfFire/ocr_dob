import os
import cv2
from datetime import datetime
import numpy as np
import re
import datefinder
from preprocess import preprocess as pre_process
import easyocr 

reader = easyocr.Reader(['en'])

regex = '(\d{2}[\.\/-]\d{2}[\/\.-]\d{2,4})'

def listToString(s):
    str1 = ""
 
    for ele in s:
        str1 += ele + ' '
 
    return str1

def dateOfBirth(image_file, threshold):
    img = pre_process(image_file, threshold)
    img = cv2.imwrite(image_file, img)
    
    data = reader.readtext(image_file, detail=0)

    result = listToString(data)

    print(result)

    date_objects = []  
    
    regex_match = re.findall(regex, result)
    print(regex_match)
    if(regex_match):
       for date_str in regex_match:
           date_str = date_str.replace('-', '/')
           date_str = date_str.replace('.', '/')
           date_obj = datetime.strptime(date_str, '%d/%m/%Y')
           date_objects.append(date_obj)

    if(date_objects):
        return str(min(date_objects).strftime("%d/%m/%Y"))
    else:
        return -1
