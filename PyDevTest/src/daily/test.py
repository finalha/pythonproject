'''
Created on 2015-7-6

@author: 16101210-15
'''

import os,sys;
fname = raw_input();
ls = os.linesep
while True:
if os.path.exists(fname):
    print(fname+'already exists')
else:
    break
