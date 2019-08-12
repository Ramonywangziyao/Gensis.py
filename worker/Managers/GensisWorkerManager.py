'''
GensisWorkerManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''


from multiprocessing.managers import BaseManager

class GensisWorkerManager(object):
    def __init__(self, ip, port_number, authkey):
        self.server_addr = ip
        self.port = port_number
        self.authkey = authkey

    def initBaseManager(self):
        BaseManager.register('get_task_queue')
        BaseManager.register('get_result_queue')

        print('[GSW] Connecting to server ', self.server_addr)

        self.manager = BaseManager(address = (self.server_addr, self.port), authkey = self.authkey.encode('utf-8'))

    def connectToMaster(self):
        if self.manager is None:
            print('[GSW] Manager not initialized.')
            exit(-1)

        try:
            self.manager.connect()

            self.taskQueue = self.manager.get_task_queue()
            self.resultQueue = self.manager.get_result_queue()
            print('[GSW] Init Worker Finished!')
            # init spider here
        except ConnectionRefusedError as e:
            print('[GSW] Master does not respond.....')
            exit(-1)

    def getTaskQueue(self):
        if self.taskQueue is None:
            print('[GSW] Task Queue not initialized.')
            return None

        return self.taskQueue

    def getResultQueue(self):
        if self.resultQueue is None:
            print('[GSW] Task Queue not initialized.')
            return None

        return self.resultQueue
