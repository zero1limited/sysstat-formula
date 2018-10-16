from datetime import datetime, timedelta

def iowait(period=10):
  
  returnData = {
    'period': period,
    'results': {},
    'average': 0
  }
  
  for daysAgo in range(0, period):
    daysAgoDate = datetime.now() - timedelta(days=daysAgo)
    returnData['results'][daysAgoDate.strftime('%Y-%m-%d')] = 'blah'
  
  return returnData
