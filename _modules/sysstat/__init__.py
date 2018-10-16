from datetime import datetime, timedelta

def iowait(period=10):
  
  returnData = {
    'period': period,
    'results': {},
    'average': 0
  }
  
  for daysAgo in range(10, 0):
    daysAgoDate = datetime.now() - timedelta(days=daysAgo)
    returnData['results'][datetime.strptime(daysAgoDate, '%Y-%m-%d')] = 'blah'
  
  return returnData
