#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist

import numpy as np
from pyquaternion import Quaternion
from scipy.spatial.transform import Rotation as R

def quaternion_to_euler_zyx(q):
    r = R.from_quat([q[0], q[1], q[2], q[3]])
    return r.as_euler('zyx', degrees=True)

def control(msg, twist_pub):#joy to twist
    q = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]
    yaw , roll , pitch = quaternion_to_euler_zyx(q)
    print(yaw, roll, pitch)

if __name__ == '__main__':
    #ノードの初期化
    rospy.init_node('gyro_correction')
    #配信準備
    twist_pub = rospy.Publisher('/joy/gyro_correction/cmd_vel', Twist, queue_size=1)
    #購読
    # rospy.Subscriber('/joy/cmd_vel', Twist, control, twist_pub)
    rospy.Subscriber('/imu/data', Imu, control, twist_pub)

    rospy.spin()