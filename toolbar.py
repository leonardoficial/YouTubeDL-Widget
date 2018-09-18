import os
import sys
import time

class Toolbar(object):
  def __init__(self):
    # get console width
    ignore, width = os.popen("stty size", "r").read().split()
    
    self.width = int(width) - 3
    self._state = 0
    
  def setup(self):
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * self.width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (self.width + 1)) # return to start of line, after '['

  def progress(self, percent):
    percent = int(percent)
    if(self._state == 100):
      print("")
   
      return 0
    
    """
    if(self._state + percent >= 100):
      _perc = int(self.width * ((percent - self._state) / 100))
    """
    
    # update the bar
    _perc = int(self.width * ((percent - self._state) / 100))
    
    sys.stdout.write("|" * _perc)
    sys.stdout.flush()
    
    self._state = percent
