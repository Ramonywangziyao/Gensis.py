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

    # the runner of analyzers. To offer an abstract way of running different analyzers on a package.
    # returns a dictionary containing results
    def analyze(self, package) -> dictionary:
        pass
