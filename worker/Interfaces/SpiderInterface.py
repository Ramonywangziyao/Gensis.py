'''
SpiderInterface.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from abc import ABC, abstractmethod

class SpiderInterface(ABC):

    @abstractmethod
    # the runner of spiders. To offer an abstract way of running different spiders.
    # return true for success operation
    # return false for failure operation
    def run(self) -> bool:
        pass
