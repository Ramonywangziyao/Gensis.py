'''
GensisWorker.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''


import sys
from multiprocessing.managers import BaseManager
from Managers.GensisWorkerManager import GensisWorkerManager
from Managers.SpiderManager import SpiderManager
from Tools.PackageAgent import PackageAgent

# usernet service start point
if sys.argv is None or len(sys.argv) == 1:
    sys.exit('[GSW] Error: you must type a service para to start AirMaster.')

service = sys.argv[1]
ip = sys.argv[2]
port_number = sys.argv[3]
authkey = sys.argv[4]

manager = GensisWorkerManager(ip, port_number, authkey)
spiderManager = SpiderManager()
packageAgent = PackageAgent(taskQueue, resultQueue)

manager.initBaseManager()
manager.connectToMaster()
taskQueue = manager.getTaskQueue()
resultQueue = manager.getResultQueue()
spiderManager.initSpiderType(service, packageAgent)
print('[GSW] Gensis Worker Spider initialization completed. Starting to crawl.......')

spiderManager.crawl()
