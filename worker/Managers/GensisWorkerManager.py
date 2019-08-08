from multiprocessing.managers import BaseManager


class GensisWorkerManager(object):
    def __init__(self):
        self.server_addr = '192.168.1.118'
        self.port = 10001
        self.authkey = 'pathea'

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
