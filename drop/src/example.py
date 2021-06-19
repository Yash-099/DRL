#!/usr/bin/env python
from utils.offboard import mavcon
import time
import rospy
rospy.init_node('offboard_node', anonymous=True)
mvc = mavcon()
mvc.setarm(1)
time.sleep(2)
mvc.offboard()
mvc.gotopose(0.0,0.0,3.25)
mvc.gotopose(0.0,5.0,3.25)
mvc.gotopose(-3.659,5.0,3.25)
mvc.gotopose(-3.659,3.36,3.25)
mvc.gotopose(-3.00,0.47,3.25)
mvc.gotopose(-1.785,-1.55,3.25)
mvc.gotopose(-2.75,-4.54,3.25)
mvc.gotopose(-4,-7,3.25)
mvc.gotopose(-4,-9,3.25)
print "last"
mvc.gotopose(-4,-9,0)
print "landed"