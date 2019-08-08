'''
SpiderManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

import sys
sys.path.append('..')
from Constants.ServiceConstants import ServiceConstants
from Tools.DataWrapper import DataWrapper
from Managers.LogManager import LogManager

class SpiderManager(object):

    # init spider manager 
    def __init__(self, service):
        self.snames = ServiceConstants()
        self.dataWrapper = DataWrapper()
        self.logManager = LogManager(service)
        self.service = service

    # crawl method. define spider crawl method here
    def crawl(self):
        print('[GS] Init service type as ', self.service)

        if self.service == self.snames.default:
            return None
