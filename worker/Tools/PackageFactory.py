import sys
sys.path.append('..')
from Packages.UsernetPackage import UsernetTaskPackage
from Packages.UsernetPackage import UsernetResultPackage
from Constants.ServiceConstants import ServiceConstants

class PackageFactory:

    def __init__(self):
        self.serviceConstants = ServiceConstants()

    def producePackage(self, service, data):
        if service == self.serviceConstants.usernetServiceName:
            return UsernetResultPackage(data)
