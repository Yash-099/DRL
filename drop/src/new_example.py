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
mvc.gotopose(-8.0,5.0,6.5) # 1st point

img = 
while True:

