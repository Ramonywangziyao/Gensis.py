'''
PackageAgent.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''


import time, threading

class PackageAgent():

    def __init__(self, taskQueue, resultQueue):
        if taskQueue is None or resultQueue is None:
            sys.exit('[GSW] Package agent initialization failed. Empty paras.')

        self.taskQueue = taskQueue
        self.resultQueue = resultQueue

    def getTask(self):
        if self.taskQueue.empty():
            print('[GSW] No more packages in task.....wait......')
            time.sleep(1)
            return None

        package = self.taskQueue.get()
        print('[GSW] Task package retrieved.')
        return package

    def putResult(self, package):
        if package is None:
            print('[GSW] No package to upload.')
            return

        print('[GSW] Result package uploaded.')
        self.resultQueue.put(package)
