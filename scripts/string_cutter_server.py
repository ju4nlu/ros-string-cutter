#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_string_cutter(req):
    result = [str[int(req.n):] for str in req.a]
    print 'Result -> ', result, '\nGive me the next one!\n'
    return StringCutterResponse(result)

def string_cutter_server():
    rospy.init_node('string_cutter_server')
    s = rospy.Service('string_cutter', StringCutter, handle_string_cutter)
    print "Ready to cut an array of strings, give it to me!"
    rospy.spin()

if __name__ == "__main__":
    string_cutter_server()