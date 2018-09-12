import os
import sys
import time

ignore, toolbar_w = os.popen("stty size", "r").read().split()

toolbar_w = int(toolbar_w) - 3

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_w))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_w + 1)) # return to start of line, after '['

for i in range(toolbar_w):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")
