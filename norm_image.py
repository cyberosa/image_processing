#!/usr/bin/env python3

import numpy as np
import imageio
import sys
from PIL import Image

def test_function():
    print("testing function")
    np.random.seed(42)

    d = np.random.uniform(5,10,[20,33]) # A 20x33 array
    max_d = np.max(d)
    min_d = np.min(d)
    norm_v = get_bw_value(d[13,13], max_d, min_d)
    i = build_dist_image(d)
    print("assert i[13,13,:] == [94 94 94]{}".format(i[13,13,:] == [94 ,94, 94]))

def get_bw_value(value, d_max, d_min):
    #  R = G = B = gray value
    norm_value = ((((value - d_min)/(d_max-d_min)))* 255.9).astype(np.uint8)

    return [norm_value, norm_value, norm_value]

def build_dist_image(dist_array):
    '''
    Method to get the black and white value for the distance
    within the given range of values
    :param dist_array:
    :return: the transformed array in the correct image format
    '''
    height, width = dist_array.shape
    t = (height, width, 3)
    print("computing max and min distance in the array")
    # furthest point --> White (255,255,255)
    d_max = np.max(dist_array)
    # closest point --> Black (0,0,0)
    d_min = np.min(dist_array)

    A = np.zeros(t, dtype=np.uint8)

    # Traverse all the depth values
    print("traversing the depth image")
    for i in range(height):
        for j in range(width):
            # Transform each value into a grey value depending on the distance
            A[i, j] = get_bw_value(dist_array[i,j], d_max, d_min)

    print("creating the image from the array")
    img = Image.fromarray(A)
    # Saving Image
    filename = 'image1.png'
    imageio.imwrite(filename, img)
    return A

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error missing input argument")

    d_array = sys.argv[1]
    if d_array == '0': # we use 0 to run the test function
        test_function()
    else:
        build_dist_image(d_array)