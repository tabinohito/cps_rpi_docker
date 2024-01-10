#!/usr/bin/env python
## coding: UTF-8
import rospy
from std_msgs.msg import String # ROS通信で文字列を取得できるようにstd_msgsというパッケージからStringという型を取得
from geometry_msgs.msg import Twist	#速度コマンドをもつ
from datetime import datetime
sim_mode = False

import os
import time

class ros_conf:
    def __init__(self):
        os.environ['ROS_MASTER_URI']='http://localhost:11311'
        os.environ['ROS_IP'] = 'localhost'
        os.environ['ROS_HOSTNAME'] = 'localhost'
        
    # def __init__(self,robot_ip_addr,host_ip_addr):
    #     os.environ['ROS_MASTER_URI']='http://{}:11311'.format(robot_ip_addr)
    #     os.environ['ROS_IP'] = host_ip_addr
    #     os.environ['ROS_HOSTNAME'] = host_ip_addr

class msg2action(ros_conf):
    def __init__(self):
        super().__init__()
        self.msg2action_init()

    # def __init__(self,robot_ip_addr,host_ip_addr):
    #     super().__init__(robot_ip_addr,host_ip_addr)
    #     self.msg2action_init()

    def msg2action_init(self):
        rospy.init_node('msg2action_bridge') # ノードの生成
        # Subscriberの作成
        self.sub = rospy.Subscriber('action', String, self.callback)
        #Twist型で'cmd_vel'というトピックを生成 rospy.Publisher('arm_robot3/cmd_vel', Twist, queue_size = 1)	#Twist型で'cmd_vel'というトピックを生成
        self.write_twist =  rospy.Publisher('arm_robot/cmd_vel', Twist, queue_size = 1)

    def callback(self, data):
        # callback関数の処理をかく
        twist = Twist()
        
        print('data is '+data.data)
        if data.data == "Right":
            twist.linear.y = -0.08
        elif data.data == "Left":
            twist.linear.y = 0.08
        elif data.data == "Forward":
            twist.linear.x = 0.08
        elif data.data == "Back":
            twist.linear.x = -0.08
            
        self.twist_publish(twist)

    def twist_publish(self, data):
        self.write_twist.publish(data)

    def function(self, data):
        # そのほかの処理もあったら書く
        return data
    
if __name__ == '__main__':

    time.sleep(3.0)
    node = msg2action()
    while not rospy.is_shutdown():
        rospy.sleep(0.1)