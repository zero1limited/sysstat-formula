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
      returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = __salt__['cmd.run'](
        cmd='sadf -d '+sarFilePath+' -- -u'
      )
    else:
      returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = {
        'average': 0,
        'message': 'Unable to find sar file'
      }
  
  return returnData
