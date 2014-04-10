#!/usr/bin/env python2
#coding: utf-8

import sys
import os
import argparse
from PIL import Image
import PIL.ImageOps

def main():
    img = open_image()
    img = convert_to_grayscale(img)
    ascii_img_array = convert_to_ascii(img)
    display(ascii_img_array)


def open_image():
    parser = argparse.ArgumentParser(description='Convert images to ASCII', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--invert', action="store_true", help="Invert image colors" , dest="is_invert")
    parser.add_argument('-r', '--reddit', action="store_true", default=False, help="Output in reddit comment formatting" , dest="is_reddit")
    parser.add_argument('file', action="store", type=str, help="File to be converted")
    parser.add_argument('--scale', type=int, help="Set sampling scale factor" , dest="scale", default=1, metavar='INT')
    args = parser.parse_args()
    global is_reddit, scale
    is_reddit = args.is_reddit
    scale = args.scale
    root,ext = os.path.splitext(args.file)
    if ext.lower() not in ['.jpg', '.jpeg', '.png', '.bmp']:
        sys.exit("Not a valid image file")
    else:
        image = Image.open(args.file)
        if args.is_invert:
            image = PIL.ImageOps.invert(image)
        return image


def convert_to_grayscale(img):
    pixel_data = img.load()
    if len(img.split()) == 4: # Image has alpha
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                # Check if opaque
                if pixel_data[x, y][3] < 255:
                    # Replace the pixel data with white
                    pixel_data[x, y] = (255, 255, 255, 255)
    return img.convert("L")


def convert_to_ascii(img):
    symbol_array = ['@', '%', '#', '*', '+', '=', '-', ':', '.']
    pixel_data = img.load()
    height = img.size[1]
    width = img.size[0]
    block_height = scale*2
    block_width = scale
    ascii_img_array = []
    for i in xrange(0, height, block_height):
        row = []
        if is_reddit:
            row.append('`')
        if i+block_height <= height:
            for j in xrange(0, width, block_width):
                avg = 0;
                if j+block_width <= width:
                    for y in xrange(i, i+block_height):
                        for x in xrange(j, j+block_width):
                            avg += pixel_data[x, y]
                    avg = avg/(block_height*block_width)
                    row.append(symbol_array[int(round((avg/255.0)*(len(symbol_array)-1)))])
            if is_reddit:
                row.append('`  ')
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