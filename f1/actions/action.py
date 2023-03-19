import os
from abc import ABC, abstractmethod

FIELDS = [
  'Driver',
  'LapTime',
  'Sector1Time',
  'Sector2Time',
  'Sector3Time',
  'Compound',
  'TyreLife',
  'FreshTyre',
  'Stint',
]

REPLACE_DAYS = '0 days '

class Action(ABC):
  def __init__(self, year, circuit, session, action):
    self.pathname = 'output/'+ "-".join([str(year), circuit, session, action]) + '.csv'

    if os.path.isfile(self.pathname):
      os.remove(self.pathname)

  @abstractmethod
  def execute(self):
    pass

  def printLap(self, lap):
    fields = []
    for field in FIELDS:
      fields.append(self.fieldToString(lap[field]))

    print(', '.join(fields))
    self.writeToCsv(', '.join(fields))


  def fieldToString(self, field):
    return str(field).replace(REPLACE_DAYS, '')

  def writeToCsv(self, line):
    with open(self.pathname, 'a') as f:
        f.write(line)
        f.write('\n')
