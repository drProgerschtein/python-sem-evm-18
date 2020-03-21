import os
import sys
import numpy as np
from imageio import imread, imwrite


def main():
    if len(sys.argv)<3:
        print('Input error')
        return -1;

    in1 = sys.argv[1]
    in2 = sys.argv[2]
    out = sys.argv[3]

    im1 = imread(in1)
    im2 = imread(in2)

    (h, w, d) = im1.shape
    if (h, w, d) == im2.shape:
        imout = np.zeros((h,w,d), dtype=np.uint8)
        for x in range(w):
            for y in range(h):
                if (im1[x][y][0]!=im2[x][y][0]) and (im1[x][y][1]!=im2[x][y][1]) and (im1[x][y][2]!=im2[x][y][2]):
                    imout[x][y]=np.uint8([255,255,255])
        imwrite(out, imout, format='jpg')
    else:
        print('Image error')

main()
