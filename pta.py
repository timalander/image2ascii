#!/usr/bin/env python2
#coding: utf-8

import sys
import os
from PIL import Image
import PIL.ImageOps

def main():
   img = open_image()
   img = convert_to_grayscale(img)
   ascii_img_array = convert_to_ascii(img)
   display(ascii_img_array)

def open_image():
    isInvert = 0
    fileArg = 1
    if len(sys.argv) == 1:
        sys.exit("No file specified")
    elif len(sys.argv) > 2:
        if sys.argv[1] == "-i":
            isInvert = 1
            fileArg = 2
        else:
            sys.exit("Please only specify one file to convert")

    root,ext = os.path.splitext(sys.argv[fileArg])
    if ext.lower() not in ['.jpg', '.jpeg', '.png', '.bmp']:
        sys.exit("Not a valid image file")
    else:
        image = Image.open(sys.argv[fileArg])
        if isInvert:
            return PIL.ImageOps.invert(image)
        else:
            return image

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
    # symbol_array = ['@', '$', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a',
    #      'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C',
    #      'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't',
    #      '/', '|', '(', ')', '1', '{', ']', '?', '-', '+', '~', '>', 'i', '!',
    #      'l', 'I', ';', ':', ',', '"', '^', '`', '.', ' ']
    symbol_array = ['@', '%', '#', '*', '+', '=', '-', ':', '.']
    pixel_data = img.load()
    height = img.size[1]
    width = img.size[0]
    block_height = 8
    block_width = 4
    ascii_img_array = []
    for i in xrange(0, height, block_height):
        row = []
        if i+block_height <= height:
            for j in xrange(0, width, block_width):
                avg = 0;
                if j+block_width <= width:
                    for y in xrange(i, i+block_height):
                        for x in xrange(j, j+block_width):
                            avg += pixel_data[x, y]
                    avg = avg/(block_height*block_width)
                    row.append(symbol_array[int(round((avg/255.0)*(len(symbol_array)-1)))])
            ascii_img_array.append(row)
    return ascii_img_array

def display(ascii_img_array):
    for x in xrange(len(ascii_img_array)):
        row = ''
        for y in xrange(len(ascii_img_array[0])):
            row += ascii_img_array[x][y]
        print row

if __name__ == "__main__":
    main()
