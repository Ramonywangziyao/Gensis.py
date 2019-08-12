'''
SpiderManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''


import sys
import time, threading
sys.path.append('..')
from Constants.ServiceConstants import ServiceConstants
from Spiders.UsernetSpider import UsernetSpider
from Tools.PackageFactory import PackageFactory

class SpiderManager(object):

    def __init__(self):
        self.snames = ServiceConstants()
        self.packageFactory = PackageFactory()
        self.totalThread = 20
        self.threadList = []
        self.lock = threading.Lock()

    def initSpiderType(self, service, packageAgent):
        self.service = service
        self.packageAgent = packageAgent

        for i in range(1, self.totalThread + 1):
            self.threadList.append(threading.Thread(target=self.threadTask, name='Thread ' + str(i), args = ()))
            print('[GSW] Thread ' + str(i) + ' created.')
            time.sleep(0.1)

        print('[GSW] Init service type as ', self.service)

    # execute interface

    def crawl(self):
        # multithreading here
        for thread in self.threadList:
            thread.start()

        for thread in self.threadList:
            thread.join()

        print('[GSW] Now executing ', self.service)


    # ------------------ End Spider Interfaces ------------------------

    def threadTask(self):
        if self.service == self.snames.default:
            pass

    # run spider for threads. use while loop to keep running state
    # More spiders to code, coming soon.............
