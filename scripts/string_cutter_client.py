#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def string_cutter_client(x, y):
    rospy.wait_for_service('string_cutter')
    try:
        string_cutter = rospy.ServiceProxy('string_cutter', StringCutter)
        resp1 = string_cutter(x, y)
        return resp1.sol
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return sys.argv[0], "[\'strings separated by spaces\' number]"

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = sys.argv[1].split()
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting array", x, "; cut from index ",y, "\n"
    print "Solution -> ", string_cutter_client(x,y)