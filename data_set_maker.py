#!usr/bin/env ipython2

import cv2 as cv
import glob

def greyscale_tifs(image_dir, new_dir):
  for mask in glob.glob(image_dir + '*.tif'):
    gmask = cv.imread(mask, cv.IMREAD_GRAYSCALE)
    _, gmask = cv.threshold(gmask, 0, 1, cv.THRESH_BINARY)
    cv.imwrite(new_dir + mask.split('/')[-1], gmask )


def main():
  greyscale_tifs( './mask/', './binary_mask/')

if __name__ == '__main__':
  main()
