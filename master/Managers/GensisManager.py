'''
GensisManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from multiprocessing.managers import BaseManager
import sys, time
sys.path.append('..')
from Managers.LogManager import LogManager
from Managers.StatManager import StatManager
from Managers.PackageManager import PackageManager
from Managers.AnalyzeManager import AnalyzeManager
from Managers.SpiderManager import SpiderManager
from Tools.PackageFactory import PackageFactory
from Tools.DataWrapper import DataWrapper
from Constants.DataTypeNames import DataTypeNames

class GensisManager(object):

    # Initialize all required managers and paras
    def __init__(self, ip, port_number, authkey, service):
        if ip is None:
            raise ValueError('[GS] Errno 0: ip address cannot be None. Gensis initilization failed.')
        if port_number is None:
            raise ValueError('[GS] Errno 0: port_number cannot be None. Gensis initilization failed.')
        if authkey is None:
            raise ValueError('[GS] Errno 0: authkey cannot be None. Gensis initilization failed.')
        if service is None:
            raise ValueError('[GS] Errno 0: service cannot be None. Gensis initilization failed.')

        self.host_ip = ip
        self.host_port = port_number
        self.authkey = authkey

        self.service = service
        self.logManager = LogManager(service)
        self.analyzeManager = AnalyzeManager(service)
        self.packageManager = PackageManager(service)
        self.packageFactory = PackageFactory()
        self.dataWrapper = DataWrapper()
        self.cnames = DataTypeNames()

    # get ready base manager for the main node. prepare for the server
    def start_gensisManager_master(self, task_queue, result_queue):
        if task_queue is None:
            raise ValueError('[GS] Errno 0: task_queue cannot be None. Gensis initilization failed.')
        if result_queue is None:
            raise ValueError('[GS] Errno 0: result_queue cannot be None. Gensis initilization failed.')

        # task distribution queue
        def _get_task_queue():
            return task_queue
        # result collection queue
        def _get_result_queue():
            return result_queue

        # map task queue and result queue to be visible for childnodes
        try:
            BaseManager.register('get_task_queue', callable = _get_task_queue)
            BaseManager.register('get_result_queue', callable = _get_result_queue)
        except BaseException as e:
            raise e('[GS] Errno 2: modular error for BaseManager. Please check your code.')

        # set up basic paras for the main node
        manager = BaseManager(address = (self.host_ip, self.host_port), authkey = self.authkey.encode('utf-8'))
        if manager is None:
            raise ValueError('[GS] Errno 0: baseManager cannot be None. Gensis initilization failed.')

        print('[GS] ', self.service, ' service created. Please wait for the next step.')
        return manager

    # task distribution process
    def package_manager_process_distribute(self, datas, task_queue, wait_queue):
        # check logger for breakpoint(new packages)
        # task_queue for uploading new tasks
        # wait_queue for failed packages
        # need to implement
        if datas is None:
            raise ValueError('[GS] Errno 0: datas cannot be None. distribution process initilization failed.')
        if task_queue is None:
            raise ValueError('[GS] Errno 0: task_queue cannot be None. distribution process initilization failed.')
        if wait_queue is None:
            raise ValueError('[GS] Errno 0: wait_queue cannot be None. distribution process initilization failed.')

        initData = datas[self.cnames.data]
        initStat = datas[self.cnames.stat]
        if initData is None:
            raise ValueError('[GS] Errno 0: initData cannot be None. distribution process initilization failed.')

        # init packages with found packages or new packages
        try:
            self.packageManager.addNewPackages(initData)
        except BaseException as e:
            raise e('[GS] Errno 2: modular error for packageManager in distribution process. Please check your code.')

        # init stat from legacy data
        if initStat != None:
            self.analyzeManager.updateStatData(initStat)

        print('[GS] Package distributor thread running.......')
        while True:
            time.sleep(1)
            try:
                while self.packageManager.hasNewPackage():
                    # get new package from manager and send it to task queue awaiting for slaves
                    new_package = packageManager.getNewPackage()
                    task_queue.put(new_package)
                    # add work end conditions. end code not completed
                    break
            except BaseException as e:
                    raise e('[GS] Errno 2: modular error for packageManager in distribution process. Please check your code.')

            # adding failed tasks
            while not wait_queue.empty():
                try:
                    print('[GS] Adding a failed package to task queue.')
                    package = wait_queue.get()
                    self.packageManager.removeVisitedPackage(package)
                except BaseException as e:
                    raise e('[GS] Errno 2: modular error for packageManager in distribution process. Please check your code.')

    # task collection process
    def package_manager_process_collect(self, conn_queue):
        # conn_queue for analyzed awaiting tasks for next execution
        if conn_queue is None:
            raise ValueError('[GS] Errno 0: conn_queue cannot be None. collection process initilization failed.')

        print('[GS] Package collector thread running.......')
        while True:
            while not conn_queue.empty():
                try:
                    datas = conn_queue.get()
                    self.packageManager.addNewPackages(datas)
                except BaseException as e:
                    raise e('[GS] Errno 2: modular error for packageManager. Please check your code.')

    # result analyze process
    def result_analysis_process(self, result_queue, conn_queue, store_queue, wait_queue):
        if result_queue is None:
            raise ValueError('[GS] Errno 0: result_queue cannot be None. analysis process initilization failed.')
        if conn_queue is None:
            raise ValueError('[GS] Errno 0: conn_queue cannot be None. analysis process initilization failed.')
        if store_queue is None:
            raise ValueError('[GS] Errno 0: store_queue cannot be None. analysis process initilization failed.')
        if wait_queue is None:
            raise ValueError('[GS] Errno 0: wait_queue cannot be None. analysis process initilization failed.')

        print('[GS] Analyzer thread running.......')
        while True:
                if not result_queue.empty():
                    res_package = result_queue.get(True)

                    if res_package.getStatus() is False:
                        print('[GS] Failure, putting package back to task queue.')
                        try:
                            task_package = self.packageFactory.regeneratePackageFromResultPackage(self.service, res_package)
                        except BaseException as e:
                            raise e('[GS] Errno 2: modular error for packageFactory. Please check your code.')

                        wait_queue.put(task_package)
                    else:
                        print('[GS] Success, start to analyze result.')
                        try:
                            wrapped_data = self.analyzeManager.analyze(res_package)
                        except BaseException as e:
                            raise e('[GS] Errno 2: modular error for analyzeManager. Please check your code.')
                        # put new packages and unprocessed packages back to queue
                        conn_queue.put(wrapped_data)
                        # store_queue.put()
                else:
                    print('[GS] Result queue is waiting for package.......')
                    time.sleep(0.5)

    # data store process
    def store_process(self, store_queue):
        if store_queue is None:
            raise ValueError('[GS] Errno 0: store_queue cannot be None. store process initilization failed.')

        print('[GS] Data manager thread running.......')
        pass
        # needs implementation.......

    # load init data
    def loadInitData(self):
        # wrapped data
        stat = None
        packed_res = dict()
        filename = 'breakpoint_' + str(self.service) + '.txt'
        data = self.logManager.loadBreakpoint(filename)

        # no breakpoint,  look for logged comments
        if data == None:
            # wrapped data
            filename = 'originUrls_' + str(self.service) + '.txt'
            urls_data = self.logManager.loadUrls(filename)

            if urls_data == None:
                spiderManager = SpiderManager(self.service)
                crawled_data = spiderManager.crawl()

                if crawled_data == None:
                    sys.exit('[GS] No data to start....Exit.....')
                else:
                    res = crawled_data
            else:
                res = urls_data
        else:
            # decode data into datas(new_urls, visited_urls), stat(stats, owners)
            res = self.dataWrapper.wrapInitData(self.service, data)
            stat = data[self.cnames.stat]

        if res != None and len(res) != 0:
            packed_res[self.cnames.data] = res
            packed_res[self.cnames.stat] = stat
            return packed_res
        else:
            return None
