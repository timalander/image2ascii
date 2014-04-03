#!/usr/bin/env python
#coding: utf-8

import sys
import os
from PIL import image


def main():
   img = open_image()

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
        img = 


if __name__ == "__main__":
    main()