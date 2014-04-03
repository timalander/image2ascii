#!/usr/bin/env python
#coding: utf-8

import sys
import os
from PIL import Image


def main():
   img = open_image()
   img = convert_to_grayscale(img)

def open_image():
    if len(sys.argv) == 1:
        print "No file specified"
        sys.exit(1)
    
    elif len(sys.argv) > 2:
        print "Please only specify one file to convert"
        sys.exit(1)
    
    root,ext = os.path.splitext(sys.argv[1])
    if ext.lower() not in ['.jpg', '.jpeg', '.png', '.bmp']:
        print "Not a valid image file"
        sys.exit(1)
    else:
        return Image.open(sys.argv[1])

def convert_to_grayscale(img):
    if len(img.split()) == 4:
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = img.split()
        img = Image.merge("RGB", (r, g, b))
    img = img.convert("L")
    img.save("out.bmp")



if __name__ == "__main__":
    main()