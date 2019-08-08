'''
PackageInterface.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from abc import ABC, abstractmethod

class PackageTaskInterface(ABC):

    @abstractmethod
    # get current status of the package: success / failure
    def getStatus(self) -> str:
        pass

    # set current status of the package: success / failure.
    # return true for success operation
    # return false for failure operation
    def setStatus(self, status) -> bool:
        pass

    # check the status of the package as success of failure
    def isSuccess(self) -> bool:
        pass

    # get data of the package
    # data is a dictionary
    def getData(self) -> dictionary:
        pass

    # set data of the package
    # data is a dictionary
    # return true for success operation
    # return false for failure operation
    def setData(self, data) -> bool:
        pass

    # get service type of the package
    def getService(self) -> str:
        pass

    # set service type of the package
    # return true for success operation
    # return false for failure operation
    def setService(self, service) -> bool:
        pass


class PackageResultInterface(metaclass=ABCMeta):

    @abstractmethod
    # get current status of the package: success / failure
    def getStatus(self) -> str:
        pass

    # set current status of the package: success / failure
    # return true for success operation
    # return false for failure operation
    def setStatus(self, status) -> bool:
        pass

    # check the status of the package as success of failure
    def isSuccess(self) -> bool:
        pass

    # get res of the package
    # res is a dictionary
    def getResult(self) -> dictionary:
        pass

    # set res of the package
    # res is a dictionary
    # return true for success operation
    # return false for failure operation
    def setResult(self, res) -> bool:
        pass

    # get service type of the package
    def getService(self) -> str:
        pass

    # set service type of the package
    # return true for success operation
    # return false for failure operation
    def setService(self, service) -> bool:
        pass
