'''
LoggerInterface.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from abc import ABC, abstractmethod

class LoggerInterface(ABC):

    @abstractmethod
    # write urls to .txt file
    # data is a dictionary
    # return true for success operation
    # return false for failure operation
    def logUrls(self, filename, data) -> bool:
        pass

    # write breakpoint to .txt file
    # data is a dictionary
    # return true for success operation
    # return false for failure operation
    def logBreakpoint(self, filename, data) -> bool:
        pass

    # load urls from .txt file
    def loadUrls(self, filename) -> dictionary:
        pass

    # load breakpoint from .txt file
    def loadBreakpoint(self, filename) -> dictionary:
        pass
