#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
from PIL import Image
import six

import imagehash

"""
Compute hash of an image
"""
def compute_hash_of_image(image_filename, hashfunc = imagehash.average_hash):
    import os
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or \
            f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f

    hash = hashfunc(Image.open(image_filename))
    print(hash);

if __name__ == '__main__':
    import sys, os
    def usage():
        sys.stderr.write("""SYNOPSIS: %s [ahash|phash|dhash|...] [<file>]

Compute the hash of an image.

Method: 
  ahash:      Average hash
  phash:      Perceptual hash
  dhash:      Difference hash
  whash-haar: Haar wavelet hash
  whash-db4:  Daubechies wavelet hash

(C) Johannes Buchner, Piercarlo Slavazza 2013-2019
""" % sys.argv[0])
        sys.exit(1)
    
    hashmethod = sys.argv[1] if len(sys.argv) > 1 else usage()
    if hashmethod == 'ahash':
        hashfunc = imagehash.average_hash
    elif hashmethod == 'phash':
        hashfunc = imagehash.phash
    elif hashmethod == 'dhash':
        hashfunc = imagehash.dhash
    elif hashmethod == 'whash-haar':
        hashfunc = imagehash.whash
    elif hashmethod == 'whash-db4':
        hashfunc = lambda img: imagehash.whash(img, mode='db4')
    else:
        usage()
    image_filename = sys.argv[2] if len(sys.argv) == 3 else usage()
    compute_hash_of_image(image_filename=image_filename, hashfunc=hashfunc)
    

