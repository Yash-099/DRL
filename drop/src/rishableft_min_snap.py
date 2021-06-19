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

mvc.gotopose(-7.504,4.968,6.5)


mvc.gotopose(-7.0,5.0,6.5) # 1frame
print "frame 1"

mvc.gotopose(-6.206934778336849, 5.172927675475209, 6.5)

mvc.gotopose(-5.651635980964664, 5.368032077183628, 6.5)



mvc.gotopose(-5.0,5.5,6.5) # 2frame
print "frame 2"

mvc.gotopose(-4.30481648361201, 5.159529647326671, 6.5)

mvc.gotopose(-3.801431008852804, 4.717130270757963, 6.5)

mvc.gotopose(-3,4,6.5) # 3frame
print "frame 3"

mvc.gotopose(-2.303000213277936, 3.467930044439495, 6.5)

mvc.gotopose(-1.554160821383733, 3.0202348023581322, 6.5)

mvc.gotopose(-0.7791612478087248, 2.6931700046208875, 6.5)


mvc.gotopose(0,2.5,6.5)# 4frame
print "frame 4"

mvc.gotopose(0.7684061210198917, 2.4422914872303028, 6.5)

mvc.gotopose(1.5203074403176655, 2.516631042664271, 6.5)

mvc.gotopose(2.2599785633892924, 2.711725892907966 ,6.5)


mvc.gotopose(3,3,6.5)# 5frame
print "frame 5"


mvc.gotopose(3.754913303245838, 3.3323044466639873 ,6.5)

mvc.gotopose(4.528535926862342 ,3.6442172188469173 ,6.5)

mvc.gotopose(5.29727478879513, 3.876471252294885 ,6.5)



mvc.gotopose(6,4,6.5)# 6frame
print "frame 6"


mvc.gotopose(6.874830329509381, 4.01559312721299, 6.5)


mvc.gotopose(7,4,6.5)# 7frame
print "last"
mvc.gotopose(-7,0,6.5)
mvc.gotopose(0,0,6.5)
mvc.gotopose(0,0,0)

print "landed"