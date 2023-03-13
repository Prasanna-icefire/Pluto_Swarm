#!/usr/bin/env
import rospy
from std_msgs.msg import String
import threading
from plutodrone.msg import *
import time

cmd = PlutoMsg()
cmd.rcRoll =1500
cmd.rcPitch = 1500
cmd.rcYaw =1500
cmd.rcThrottle =1000
cmd.rcAUX1 =1500
cmd.rcAUX2 =1500
cmd.rcAUX3 =1500
cmd.rcAUX4 =1500
cmd.commandType = 0
cmd.trim_roll = 0
cmd.trim_pitch = 0
cmd.isAutoPilotOn = 0

def Disarm():
    time.sleep(5)
    global cmd
    cmd.rcAUX4=1000

t = threading.Thread(target=Disarm)
t.start()



def talk_to_me():
    command_pub = rospy.Publisher('/drone_command', PlutoMsg, queue_size=1)    
    rospy.init_node('publish_rc_channels', anonymous=True)#Name of the node
    rate = rospy.Rate(1)
    rospy.loginfo("RC_Channels_Publishing now")
    while not rospy.is_shutdown():
        command_pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass