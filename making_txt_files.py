import rosbag
import numpy as np
#import statistics
#bag = rosbag.Bag("/home/aanal/present/Lshape_withoutwalls_hover.bag")
bag = rosbag.Bag("part_2.bag")


groundx = []
groundy = []
groundz = []

velx = []
vely = []
velz = []
pose_time = []
linear_vel_x = []
linear_vel_y = []
linear_vel_z = []
velocity = []
pose_x = []
pose_y = []
pose_z = []

for topic, msg, t in bag.read_messages(topics = '/gazebo/model_states'):
	pose_time.append(t)
	n = list(msg.name).index('iris')
	velocity.append((msg.twist[n].linear.x)**2 + (msg.twist[n].linear.y)**2 + (msg.twist[n].linear.z)**2)
	pose_x.append(msg.pose[n].position.x)
	pose_y.append(msg.pose[n].position.y)
	pose_z.append(msg.pose[n].position.z)

	linear_vel_x.append(msg.twist[n].linear.x)
	linear_vel_y.append(msg.twist[n].linear.y)
	linear_vel_z.append(msg.twist[n].linear.z)
	print(t)
	#print(msg.pose.position.y)
	#print(msg.pose.position.z)

image_time = []
for topic, msg, t in bag.read_messages(topics = '/r200/rgb/image_raw'):
	#n = list(msg.name).index('iris')	
#	if float(str(t))/10**9>305:
#		break
	image_time.append(t)
	#groundx.append(msg.pose[n].position.x)
	#groundy.append(msg.pose[n].position.y)
	#groundz.append(msg.pose[n].position.z)
	#velx.append(msg.twist[n].linear.x)
	#vely.append(msg.twist[n].linear.y)
	#velz.append(msg.twist[n].linear.z)
#print(msg.name)
linear_vel_x_final = []
linear_vel_y_final = []
linear_vel_z_final = []
linear_vel_mag_final = []

pose_x_final = []
pose_y_final = []
pose_z_final = []
j = 0
for i in range(len(image_time)):
	for q in range(j,len(pose_time)):
		if pose_time[q]>image_time[i]:
			linear_vel_x_final.append(linear_vel_x[q])
			linear_vel_y_final.append(linear_vel_y[q])
			linear_vel_z_final.append(linear_vel_z[q])
			linear_vel_mag_final.append(np.sqrt((linear_vel_x[q])**2 + (linear_vel_y[q])**2 + (linear_vel_z[q])**2))
			pose_x_final.append(pose_x[q])
			pose_y_final.append(pose_y[q])
			pose_z_final.append(pose_z[q])

			j=q
			break





for k in range(len(pose_x_final)):
	file1 = open("pose/"+str(image_time[k])+".txt","w")
	L = [str(pose_x_final[k]),str(pose_y_final[k]),str(pose_z_final[k]),str(linear_vel_mag_final[k])]
	file1.write(L[0]+'\n')
	file1.write(L[1]+'\n')
	file1.write(L[2]+'\n')
	file1.write(L[3]+'\n')
	print("file "+" pose/"+str(image_time[k])+".txt"+" written")





#	break

# for topic, msg, t in bag.read_messages(topics = '/mavros/vision_pose/pose'):
# 	ground_time.append(t)
# 	groundx.append(msg.pose.position.x)
# 	groundy.append(msg.pose.position.y)
# 	groundz.append(msg.pose.position.z)
