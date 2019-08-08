'''
DataManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

import sys
sys.path.append('..')
from Constants.ServiceTypeNames import ServiceTypeNames

class DataStorageManager(object):

    def __init__(self, service):
        if service is None:
            raise ValueError('[GS] Errno 0: service cannot be None. Data Storage initilization failed.')

        self.service = service
        self.snames = ServiceTypeNames()

    # assign data storage tools based on service types
    def initDataStorager(self):
        if self.service == self.snames.default:
            self.dataStorager = None
        # add more cases here...........

'''
    Not yet completed here. Wait for the next update. Thanks!
    
    def write(self):
        pass

    def search(self):
        pass

    def isExist(self):
        pass

    def delete(self):
        pass
'''
