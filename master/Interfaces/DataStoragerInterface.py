'''
AnalyzerInterface.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from abc import ABC, abstractmethod

class AnalyzerInterface(ABC):

    @abstractmethod
    # init with service name
    def __init__(self, service):
        pass

    # write single data to disk
    def writeDataToDisk(self, data: dictionary) -> bool:
        pass

    # write multiple data to disk
    def writeMultipleDataToDisk(self, datas: array) -> bool:
        pass

    # read single data from disk
    def readDataFromDisk(self, identifier) -> dictionary:
        pass

    # read multiple data from disk
    def readMultipleDataFromDisk(self, identifiers: array) -> array:
        pass

    # delete a data from disk
    def deleteFromDisk(self, identifier) -> bool:
        pass

    # look for a data
    def checkForExist(self, identifier) -> bool:
        pass
