from datetime import datetime, timedelta
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import csv
import os

def iowait(period=10):

  returnData = {
    'period': period,
    'results': {},
    'average': 0
  }

  runningTotal = 0
  totalResults = 0

  for daysAgo in range(0, period):
    daysAgoDate = datetime.now() - timedelta(days=daysAgo)

    # todo comeback to and check for other file paths
    sarFilePath = '/var/log/sysstat/sa' + daysAgoDate.strftime('%Y%m%d')
    if os.path.isfile(sarFilePath):
      sarData = StringIO(__salt__['cmd.run'](
        cmd='sadf -d '+sarFilePath+' -- -u'
      ))
      reader = csv.reader(sarData, delimiter=';')
      rowCount = 0
      ioWaitColumn = 0
      columnCount = 0
      totalIOWait = 0
      for row in reader:
        # for some reason we can have 2 or more sets of headers
        if '%iowait' in row :
            ioWaitColumn = row.index('%iowait')
            columnCount = len(row)
            continue


        # haven't found a column yet
        if columnCount == 0 or columnCount != len(row) :
            continue

        totalIOWait += float(row[ioWaitColumn])
        rowCount += 1

      returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = {
        'fail': False,
        'average': (totalIOWait / (rowCount - 2)),
        'data_set_size': (rowCount - 2)
      }
      runningTotal += (totalIOWait / (rowCount - 2))
      totalResults += 1
    else:
      returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = {
        'fail': True,
        'average': 0,
        'message': 'Unable to find sar file'
      }

  returnData['average'] = (runningTotal / totalResults)
  return returnData
