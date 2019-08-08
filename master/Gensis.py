'''
Gensis.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

from multiprocessing.managers import BaseManager
from multiprocessing import Process, Queue
from Managers.DataManager import DataManager
from Managers.PackageManager import PackageManager
from Managers.SpiderManager import SpiderManager
from Managers.LogManager import LogManager
from Managers.AnalyzeManager import AnalyzeManager
from Managers.GensisManager import GensisManager

if __name__ == '__main__':
    # init queues
    # terminal paras: argv[0]: serviceType, argv[1]: gameId (opt)
    # awaiting package to be crawled
    task_queue = Queue()
    # received Package results from slave nodes
    result_queue = Queue()
    # awaiting results to be stored
    store_queue = Queue()
    # awaiting results to be analyzed or calculated
    conn_queue = Queue()

    wait_queue = Queue()


    # usernet service start point
    if sys.argv is None or len(sys.argv) == 1:
        sys.exit('[GS] Error: you must type a service para to start AirMaster.')

    service = sys.argv[1]

    manager = GensisManager(service)
    master = manager.start_gensisManager_master(task_queue, result_queue)

    # init processes
    datas = manager.loadInitData()
    if datas is None:
        sys.exit('[GS] No data is loaded. Error or task has completed.')


    # init tunnels
    package_manager_process_distribute = Process(target = manager.package_manager_process_distribute, args = (datas, task_queue, wait_queue,))
    package_manager_process_collect = Process(target = manager.package_manager_process_collect, args = (conn_queue,))
    result_analysis_process = Process(target = manager.result_analysis_process, args = (result_queue, conn_queue, store_queue, wait_queue,))
    store_process = Process(target = manager.store_process, args = (store_queue,))

    package_manager_process_distribute.start()
    package_manager_process_collect.start()
    result_analysis_process.start()
    store_process.start()

    package_manager_process_distribute.join()
    package_manager_process_collect.join()
    result_analysis_process.join()
    store_process.join()

    master.get_server().serve_forever()
