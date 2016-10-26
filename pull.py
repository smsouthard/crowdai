#!/usr/bin/env ipython2
import urllib2
import urllib

## Generate image file lists
def file_list_reader(url):
  ok = urllib2.urlopen(url)
  ok = ok.readlines()
  return map(str.strip, ok)


## download image

def downloader(image_dir, image_list):
  for image in image_list:
    urllib.urlretrieve(image, image_dir + image.split('/')[-1])

def main():

  maskurl = 'https://s3.amazonaws.com/crowdai-ml-challenge/masks_urls.txt'
  tileurl = 'https://s3.amazonaws.com/crowdai-ml-challenge/tiles_urls.txt'
  maskdir = './mask/'
  tiledir = './tiles/'

  masklist = file_list_reader(maskurl)
  tilelist = file_list_reader(tileurl)

  downloader(maskdir, masklist)
  downloader(tiledir, tilelist)


if __name__ == '__main__':
  main()
