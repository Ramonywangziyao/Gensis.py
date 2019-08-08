'''
LogManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

import time
import os
import errno
import sys
sys.path.append('..')
from Constants.ServiceConstants import ServiceConstants

class LogManager(object):

    # init logManager
    def __init__(self, service):
        self.snames = ServiceConstants()
        self.service = service
        self.logger = None

        # assign customized logger
        if service == self.snames.default:
            self.logger = None

    # log urls to txt file
    # urls for spider usage
    def logUrls(self, name, gameId, urls, flag):
        if self.logger is None:
            print('[GS] Error: Logger not initialized.')
            return None

        self.logger.logUrls(name, gameId, urls, flag)

    # log breakpoint for next execution
    def logBreakpoint(self, name, data, gameId, flag):
        if self.logger is None:
            print('[GS] Error: Logger not initialized.')
            return None

        self.logger.logBreakpoint(name, data, gameId, self.service, flag)

    # load urls from txt file
    def loadUrls(self, name):
        if self.logger is None:
            print('[GS] Error: Logger not initialized.')
            return None

        return self.logger.loadUrls(name)

    # load breakpoint from last execution
    def loadBreakpoint(self, name):
        if self.logger is None:
            print('[GS] Error: Logger not initialized.')
            return None

        return self.logger.loadBreakpoint(name)
