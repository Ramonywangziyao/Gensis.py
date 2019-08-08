'''
AnalyzeManager.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''

import sys
sys.path.append('..')
from Constants.ServiceTypeNames import ServiceTypeNames
from Constants.DataTypeNames import DataTypeNames
from Managers.StatManager import StatManager
from Tools.DataWrapper import DataWrapper

class AnalyzeManager(object):

    # Initilization
    # snames is Enum of service names
    # cnames is Enum of key names
    # statTool is used for statistic analyze for specific usage
    # data wrapper is for data wrapping as input or output
    def __init__(self, service):
        if service is None:
            raise ValueError('[GS] Errno 0: service cannot be None. Analyzer initilization failed.')

        self.service = service
        self.snames = ServiceTypeNames()
        self.cnames = DataTypeNames()
        self.statTool = StatManager().assignStatTool(service)
        self.dataWrapper = DataWrapper()
        self.initAnalyzer()

    # assign analyzers based on service types
    def initAnalyzer(self):
        if self.service == self.snames.default:
            self.analyzer = None
        # add more cases here...........

    # run analyze
    def analyze(self, package) -> dictionary:
        if package is None:
            raise ValueError('[GS] Errno 0: package cannot be None. Analyze failed.')
        if self.service is None:
            raise ValueError('[GS] Errno 0: service cannot be None. Analyze failed.')
        if self.analyzer is None:
            raise ValueError('[GS] Errno 0: analyzer cannot be None. Analyze failed.')

        # extract analyzed data
        res = self.analyzer.analyze(package)
        if res is None:
            raise ValueError('[GS] Errno 0: res cannot be None')

        analyzedRes = res[self.cnames.wrapped]
        statRes = res[self.cnames.stat]

        self.updateStatData(statRes)

        return analyzedRes

    # update stat
    def updateStatData(self, stat):
        if stat is None:
            raise ValueError('[GS] Errno 0: stat cannot be None. Update failed.')
        if self.statTool is None:
            raise ValueError('[GS] Errno 0: statTool cannot be None. Update failed.')

        updateStatStatus = self.statTool.updateStat(stat)
        if updateStatStatus is False:
            raise ChildProcessError('[GS] Errno -1: update statistic failed. Please check for StatTool.updateStat().')

    # get current stat
    def getCurrentStat(self) -> dictionary:
        if self.statTool is None:
            raise ValueError('[GS] Errno 0: statTool cannot be None. Get stat data failed.')

        curStat = self.statTool.getStat()
        if curStat is None:
            raise ValueError('[GS] Errno 0: curStat found None. Stat error. Please check your StatTool.')

        return curStat

    # print current stat
    def printCurrentStat(self):
        if self.statTool is None:
            raise ValueError('[GS] Errno 0: statTool cannot be None. Print stat failed.')

        self.statTool.printStat()


    # ------------------ End Analyzer Interfaces ------------------------
