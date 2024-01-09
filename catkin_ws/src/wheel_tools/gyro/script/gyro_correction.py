#! /usr/bin/env python3

import rospy
import time
from sensor_msgs.msg import Joy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist

import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R

class gyro_node():
    def __init__(self):
        self.sub_joystick = rospy.Subscriber('/joy/cmd_vel', Twist, self.get_joystick)
        self.sub_imu = rospy.Subscriber('/imu/data', Imu, self.control)
        self.pub_control = rospy.Publisher('/joy/gyro_correction/cmd_vel', Twist, queue_size=1)

        self.joystick = None
        self.initial_orientation = None
        self.orientation_prev =None

        self.kp = 0.1

    def get_joystick(self,msg):
        self.joystick = msg

    def control(self, msg):#joy to twist
        q = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]
        yaw , roll , pitch = self.quaternion_to_euler_zyx(q)
        if self.initial_orientation is None:
            self.initial_orientation = yaw , roll , pitch
        else:
            yaw -= self.initial_orientation[0]
            roll -= self.initial_orientation[1]
            pitch -= self.initial_orientation[2]

            yaw_diff = yaw - self.orientation_prev[0]
            

        self.orientation_prev = yaw , roll , pitch        
        print(yaw)

    def quaternion_to_euler_zyx(self,q):
        r = R.from_quat([q[0], q[1], q[2], q[3]])
        return r.as_euler('zyx')

if __name__ == '__main__':
    rospy.init_node('gyro_correction')

    time.sleep(3.0)
    node = gyro_node()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)