import urllib2
import urllib

maskurl = 'https://s3.amazonaws.com/crowdai-ml-challenge/masks_urls.txt'
tileurl = 'https://s3.amazonaws.com/crowdai-ml-challenge/tiles_urls.txt'

## Generate image file lists
def file_list_reader(url):
  ok = urllib2.urlopen(url)
  ok = ok.readlines()
  return map(str.strip, ok)


## download image

def downloader(image_dir, image_list):
  for image in image_list:
    urllib.urlretrieve(image, image_dir + image.split('/')[-1])
