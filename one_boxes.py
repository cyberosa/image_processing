#!/usr/bin/env python3

import numpy as np
import sys

def test_function():
    print("testing function")
    np.random.seed(42)

    im = np.random.random_integers(200,300,[5,5,1]) # A 5X5 array
    print("array before")
    print(im)
    print("shape {}".format(im.shape))
    bo = [(2,1,4,3)]
    om = fill_with_ones(im, bo)
    print("array after")
    print(om)

def fill_with_ones(im_array, boxes):
    '''
    Create a python method that takes a binary numpy array ( w x h x 1 )
    and a sequence of box coordinates (x1,y1,x2,y2) as input and fills
    the input array with ones for the regions covered by the boxes in the sequence
    and zeros for everything else
    :param im_array: binary numpy array ( w x h x 1 )
    :param boxes: sequence of box coordinates (x1,y1,x2,y2)
    :return: the transformed image
    '''
    w,h,d = im_array.shape
    # initialize the output array
    output = np.zeros((w,h,d))
    # put ones only in the coordinates specified by the boxes
    for box in boxes:
        x1, y1, x2, y2 = box
        # considering that the x coordinates are always between 0 and w-1
        # considering that the y coordinates are always between 0 and h-1
        # considering that x2 is always > x1
        # considering that y2 is always > y1
        output[x1:x2+1,y1:y2+1,:] = 1
    return output


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Error missing input argument")

    im_array = sys.argv[1]
    boxes = sys.argv[2]
    if im_array == '0': # we use 0 to run the test function
        test_function()
    else:
        fill_with_ones(im_array, boxes)