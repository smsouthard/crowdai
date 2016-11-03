#!usr/bin/env ipython

import cv2 as cv
import glob
import os
import random
import shutil

def greyscale_tifs(image_dir, new_dir):
  for mask in glob.glob(image_dir + '*.tif'):
    gmask = cv.imread(mask, cv.IMREAD_GRAYSCALE)
    _, gmask = cv.threshold(gmask, 0, 1, cv.THRESH_BINARY)
    cv.imwrite(new_dir + mask.split('/')[-1], gmask )

def sample_set(image_dir, mask_dir ):
  values = {'test':.20, 'cv':.20}
  imagecount = len(glob.glob(mask_dir + '*.tif'))

  for group in values:
    values[group] *= imagecount
    filenames = glob.glob(mask_dir + '*.tif')
    filenames_random = random.sample(filenames, int(round(values[group])))

    for i in filenames_random:
      ff = i.split('/')[-1]
      os.rename(i,'./'+group+'/'+'binary_mask/'+ff)
      shutil.copyfile('./tiles/'+ff,'./'+group+'/'+'tiles/'+ff)

    #training handling
  for i in glob.glob(mask_dir + '*.tif'):
    ff = i.split('/')[-1]
    os.rename(i,'./train/binary_mask/'+ff)
    shutil.copyfile('./tiles/'+ff,'./train/tiles/'+ff)

def trimmer(image_dir):
  for mask in glob.glob(image_dir + '*.tif'):
    img = cv.imread(mask)
    cv.imwrite(mask, img[0:406, 0:406])


def main():
  trimmer('./mask/')
  trimmer('./tiles')
  greyscale_tifs( './mask/', './binary_mask/')
  sample_set('./tiles/' , './binary_mask/')
 


if __name__ == '__main__':
  main()
