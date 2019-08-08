import sys
import time, threading
sys.path.append('..')
from Constants.ServiceConstants import ServiceConstants
from Spiders.UsernetSpider import UsernetSpider
from Tools.PackageFactory import PackageFactory

class SpiderManager(object):

    def __init__(self):
        self.serviceConstants = ServiceConstants()
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
        if self.service == self.serviceConstants.usernetServiceName:
            self.runUsernetSpider()

    def runUsernetSpider(self):
        threadName = str(threading.current_thread().name)

        while True:
            # concurrency
            # get url
            self.lock.acquire()
            try:
                # get a package
                task_package = self.packageAgent.getTask()
            finally:
                self.lock.release()

            if task_package is None:
                time.sleep(1)
                continue

            gameId = task_package.getGameId()
            # needs package decoder
            # package decode
            us = UsernetSpider(task_package.getUrl(), threadName, gameId)
            result = us.run()
            
            res_package = self.packageFactory.producePackage(self.service, result)
            # pur url
            self.lock.acquire()
            try:
                self.packageAgent.putResult(res_package)
            finally:
                self.lock.release()



    # More spiders to code, coming soon.............
