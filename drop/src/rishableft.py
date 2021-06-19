from utils.offboard import mavcon
import time
import rospy
rospy.init_node('offboard_node', anonymous=True)
mvc = mavcon()
mvc.setarm(1)
time.sleep(2)
mvc.offboard()
mvc.gotopose(0.0,0.0,6.5)
mvc.gotopose(-8.0,0.0,6.5)
mvc.gotopose(-8.0,5.0,6.5)
mvc.gotopose(-7.0,5.0,6.5)
mvc.gotopose(-5.0,5.5,6.5)
mvc.gotopose(-3,4,6.5)
mvc.gotopose(0,2.5,6.5)
mvc.gotopose(3,3,6.5)
mvc.gotopose(6,4,6.5)
mvc.gotopose(7,4,6.5)
print "last"
mvc.gotopose(-7,0,6.5)
mvc.gotopose(0,0,6.5)
mvc.gotopose(0,0,0)

print "landed"