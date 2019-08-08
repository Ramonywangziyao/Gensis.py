'''
StatToolsInterface.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from abc import ABC, abstractmethod

class StatToolsInterface(ABC):

    @abstractmethod
    # update current stat data or init from statData
    # return true for success operation
    # return false for failure operation
    def updateStat(self, statData) -> bool:
        pass

    # get current stat data
    def getStat(self) -> dictionary:
        pass

    # print stat data
    def printStat(self):
        pass
