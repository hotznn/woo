import random
from datetime import datetime


def now():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  
def uuid():
  id = ""
  for i in range(40):
    id = id + random.choice('0123456789')
  return id
  
def fullid():
  return datetime.now().strftime('%Y%m%d') + uuid()
  
