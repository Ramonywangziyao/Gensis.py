import sys
from multiprocessing.managers import BaseManager
from Managers.GensisWorkerManager import GensisWorkerManager
from Managers.SpiderManager import SpiderManager
from Tools.PackageAgent import PackageAgent

# usernet service start point
if sys.argv is None or len(sys.argv) == 1:
    sys.exit('[GSW] Error: you must type a service para to start AirMaster.')

service = sys.argv[1]

manager = GensisWorkerManager()
spiderManager = SpiderManager()
packageAgent = PackageAgent(taskQueue, resultQueue)

manager.initBaseManager()
manager.connectToMaster()
taskQueue = manager.getTaskQueue()
resultQueue = manager.getResultQueue()
spiderManager.initSpiderType(service, packageAgent)
print('[GSW] Gensis Worker Spider initialization completed. Starting to crawl.......')

spiderManager.crawl()
