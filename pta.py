#!/usr/bin/env python
#coding: utf-8

import sys
import os
from PIL import Image


def main():
   img = open_image()
   img = convert_to_grayscale(img)
   ascii_img_array = convert_to_ascii(img)


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
    pixel_data = img.load()
    if len(img.split()) == 4: # Image has alpha
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                # Check if opaque
                if pixel_data[x, y][3] < 255:
                    # Replace the pixel data with the color white
                    pixel_data[x, y] = (255, 255, 255, 255)
    return img.convert("L")

def convert_to_ascii(img):
    symbol_array = ['@', '$', 'B', '%', '8', '&', 'W', 'M', '#', '*' 'o', 'a',
         'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C',
         'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', 
         '/', '|', '(', ')', '1', '{', ']', '?', '-', '+', '~', '>', 'i', '!', 
         'l', 'I', ';', ':', ',', '"', '^', '`', '.']
    pixel_data = img.load()
    height = img.size[1]
    width = img.size[0]
    box_height = 5
    box_width = 3

    




if __name__ == "__main__":
    main()