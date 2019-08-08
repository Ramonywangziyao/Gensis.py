'''
DataWrapper.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

import sys
sys.path.append('..')
from Constants.DataTypeNames import DataTypeNames
from Constants.ServiceTypeNames import ServiceTypeNames

class DataWrapper():

    # init data wrapper
    def __init__(self):
        self.cnames = DataTypeNames()
        self.snames = ServiceTypeNames()

    # wrap method.
    # define a wrap method for specific usage and run here
    def wrapInitData(self, service, data):
        if service == self.snames.default:
            return None
