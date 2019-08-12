'''
PackageFactory.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''


import sys
sys.path.append('..')
from Packages.UsernetPackage import UsernetTaskPackage
from Packages.UsernetPackage import UsernetResultPackage
from Constants.ServiceConstants import ServiceConstants

class PackageFactory:

    def __init__(self):
        self.snames = ServiceConstants()

    def producePackage(self, service, data):
        if service == self.snames.default:
            return None
