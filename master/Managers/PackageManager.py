'''
PackageManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

try:
    import cPickle as pickle
except:
    import pickle
import hashlib
import time, threading
import sys
sys.path.append('..')
from Managers.LogManager import LogManager
from Tools.PackageFactory import PackageFactory
from Constants.DataTypeNames import DataTypeNames

class PackageManager(object):

    # init package manager
    # package manager manages two set:
    # 1: new packages 2: visited packages
    def __init__(self, service):
        if service is None:
            raise ValueError('[GS] Errno 0: service cannot be None. Analyzer initilization failed.')

        self.new_packages = set()
        self.visited_packages = set()
        self.service = service
        self.cnames = DataTypeNames()
        self.logManager = LogManager(service)
        self.packageFactory = PackageFactory()

    # check package validation
    def isValidPackage(self, package):
        if package is None:
            raise ValueError('[GS] Errno 0: package cannot be None. Analyzer initilization failed.')

        if package.getUrl() is None:
            return False

        # add package validation code here
        return True

    # check whether a package contains content or url that had seen
    def isBrandNewPackage(self, package):
        if self.isValidPackage(package) is False:
            return None

        package_md5 = self.getEncryptedCode(package)
        if package not in self.new_packages and package_md5 not in self.visited_packages:
            return True
        else:
            return False

    # get encrypted package code.
    # uses md5 encyption on url
    def getEncryptedCode(self, package):
        if self.isValidPackage(package) is False:
            return None
        encryptor = hashlib.md5()
        encryptor.update(package.getUrl().encode('utf-8'))
        package_md5 = encryptor.hexdigest()
        return package_md5

    # check whether there are new packages
    def has_new_package(self):
        return self.new_package_size() != 0

    # get a new package from front of new package queue
    def get_new_package(self):
        package = self.new_packages.pop()
        self.add_visited_package(package)
        return package

    # add a new package to the end of new package queue
    def add_new_package(self, package):
        if self.isValidPackage(package) is False:
            time.sleep(1)
            return

        if self.isBrandNewPackage(package):
            self.new_packages.add(package)

    # add a vsited package to the end of visited package queue
    def add_visited_package(self, package):
        if not self.isValidPackage(package):
            return

        package_md5 = self.getEncryptedCode(package)
        if package_md5 not in self.visited_packages:
            self.visited_packages.add(package_md5)

    # remove a visited package from visited package queue
    def remove_visited_package(self, package):
        if not self.isValidPackage(package):
            return

        package_md5 = self.getEncryptedCode(package)
        if package_md5 in self.visited_packages:
            self.visited_packages.remove(package_md5)
        self.add_new_package(package)

    # add a group of new packages,
    # init from raw data, and create packages
    def add_new_packages(self, datas):
        urls = datas[self.cnames.urls]
        old_urls = datas[self.cnames.old_urls]
        service = datas[self.cnames.service]
        data = datas[self.cnames.data]
        flag = datas[self.cnames.flag]

        if urls is None or len(urls) == 0:
            return

        for url in urls:
            package = self.packageFactory.producePackage(service, flag, url, data)
            self.add_new_package(package)

        if old_urls != None:
            for url in old_urls:
                package = self.packageFactory.producePackage(service, flag, url, data)
                self.add_visited_package(package)

    # add a group of visited packages
    def add_visited_packages(self, packages):
        if packages is None or len(packages) == 0:
            return

        for package in packages:
            self.add_visited_package(package)

    # get current new package queue length
    def new_package_size(self):
        return len(self.new_packages)

    # get current visited package queue length
    def visited_package_size(self):
        return len(self.visited_packages)

    def save_process(self, path, data):
        pass

    def load_process(self, path):
        pass
