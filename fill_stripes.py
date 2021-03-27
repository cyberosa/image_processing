#!/usr/bin/env python3

import numpy as np
import sys
import imageio
from PIL import Image, ImageDraw

def test_function():
    print("testing function")
    np.random.seed(42)
    filename = 'im_stripes.png'
    im = fill_with_stripes(2, (100, 100), 'im_2_100_100.png')
    im = fill_with_stripes(10, (500, 500), 'im_10_500_500.png')
    im = fill_with_stripes(13, (350, 400), 'im_13_350_400.png')
    im = fill_with_stripes(0, (350, 200), 'im_0_350_200.png')
    im = fill_with_stripes(10, (-350, 200), 'error.png')

def fill_with_stripes(nr_stripes, size, filename):
    '''
    Create a Python function that returns a Numpy array representing an image
    with vertical black and white stripes.
    width of the stripe has not been specified so we assume is one pixel
    to simplify the problem
    :param nr_stripes: number of stripes in the image
    :param size: size of the image in height and width
    :param filename: name of the image file to save
    :return: the requested image
    '''
    h, w = size
    if h <= 0 or w <= 0:
        print("non valid parameters")
        return None
    # initialize the output array
    t = (h, w, 3)
    # by default all black
    A = np.zeros(t, dtype=np.uint8)
    # all odd positions in w will be white
    # total number of odd columns
    total_odds = w // 2
    if w % 2 != 0:
        total_odds += 1 # nr of white columns is always one more
    # ::2 = all odd cols
    # we  need just a column every w // nr_stripes - 1
    if nr_stripes > 0:
        n = (w // nr_stripes) -1
        A[:,::n,:] = [255, 255, 255]

    print("creating the image from the array")
    img = Image.fromarray(A)
    # Saving Image
    imageio.imwrite(filename, img)

    return A


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Error missing input argument")

    nr_stripes = sys.argv[1]
    height = sys.argv[2]
    width = sys.argv[3]
    filename = sys.argv[4]
    if nr_stripes == '-1': # we use -1 to run the test function
        test_function()
    else:
        fill_with_stripes(nr_stripes, (height,width), filename)