import rospy
from sensor_msgs.msg import Image
# from std_msgs.msg import String
from gazebo_msgs.msg import ModelStates
from cv_bridge import CvBridge
import cv2
from utils.offboard import mavcon
import time
import rospy


# from drl_pytorch import *
br = CvBridge()
# model = DRL_model()
# model.load_state_dict(torch.load('dronet.pth',map_location=torch.device('cpu'))
## loading weights

pose_x = 0
pose_y = 0
pose_z = 0



def callback(data):
	img = br.imgmsg_to_cv2(data)
	print(img.shape)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	temp = cv2.resize(gray,(200,200))
	# x,y,v = model(temp)
	x,y,v = 2,3,4
	rospy.sleep(0.1) 
	gotopose(pose_x+0.1*x,pose_y+0.1*y,6.5)

def callback_2(data):
	pose_x = float(data.pose[1].position.x)
	pose_y = float(data.pose[1].position.y)
	pose_z = float(data.pose[1].position.z)
	print(x,type(x))
	print('hello')

def listener():
	rospy.init_node('listener',anonymous=True)
	rospy.Subscriber('/gazebo/model_states',ModelStates,callback_2)
	rospy.Subscriber('/r200/rgb/image_raw',Image,callback)
	rospy.spin()




if __name__=="__main__":
	print('hii')
	rospy.init_node('offboard_node', anonymous=True)
	print('hi')
	mvc = mavcon()
	mvc.setarm(1)
	time.sleep(2)
	print('hi')
	mvc.offboard()
	print('hi')
	mvc.gotopose_new(0.0,0.0,6.5)
	mvc.gotopose_new(-8.0,0.0,6.5)
	mvc.gotopose_new(-8.0,5.0,6.5) # 1st point
	listener()