from datetime import datetime, timedelta
from StringIO import StringIO
import csv
import os

def iowait(period=10):
  
  returnData = {
    'period': period,
    'results': {},
    'average': 0
  }
  
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
      totalIOWait = 0
      for row in reader:
        rowCount += 1
        if rowCount == 0:
          continue
        elif rowCount == 1:
          ioWaitColumn = row.index('%iowait')
          continue
        else:
          totalIOWait += float(row[ioWaitColumn])
      
      returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = {
        'average': (totalIOWait / (rowCount - 2))
      }
    else:
      returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = {
        'average': 0,
        'message': 'Unable to find sar file'
      }
  
  return returnData
