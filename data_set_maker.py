#!usr/bin/env ipython2

import cv2 as cv
import glob
import os
import random
import shutil.copytree

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
      shutil.copytree('./tiles/'+ff,'./'+group+'/'+'test/'+ff)

  #training handling
  filenames = glob.glob(mask_dir + '*.tif')
  ff = filenames.split('/')[-1]
  os.rename(i,'./'+group+'/'+'binary_mask/'+ff)
  shutil.copytree('./tiles/'+ff,'./'+group+'/'+'test/'+ff)


def main():
  greyscale_tifs( './mask/', './binary_mask/')

if __name__ == '__main__':
  main()
