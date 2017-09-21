import numpy as np
import sys, os

name = '--DwgB78t-c';

trainval = 'train-feat/';
featfile = trainval + name + '.feat.bin'

feat = np.fromfile(featfile, 'f4')
print feat
print feat.shape
