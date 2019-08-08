'''
DataTypeNames.py
Gensis

Tested with Python 3.7.4
Version 1.0.0 - tonywangziyao@gmail.com

Created by Ziyao Wang on 07/01/2019
Copyright @ 2019 Ziyao Wang. All right reserved.
'''


from enum import Enum

class DataTypeNames(Enum):

    # ID of a specific game on Steam
    gameId = 'gameId'

    # data as a wrapped item for a specific usage
    data = 'data'

    # single url, contains only one url
    url = 'url'

    # multiple urls (url set or array)
    urls = 'urls'

    # flag for single functional purpose
    flag = 'flag'

    # flag list for multiple functional purposes
    flags = 'flags'

    # service means a specific functionality you defined, includes a group of spiders, analyzers, loggers, etc
    service = 'service'

    # status for success or failure for package received or not
    status = 'status'

    # wrapped data
    wrapped = 'wrapped_data'

    # stat data
    stat = 'stat'
    # and more..........
