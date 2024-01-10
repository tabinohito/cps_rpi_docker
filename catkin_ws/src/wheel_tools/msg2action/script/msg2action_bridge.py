#!/usr/bin/env python
## coding: UTF-8
import rospy
from std_msgs.msg import String # ROS通信で文字列を取得できるようにstd_msgsというパッケージからStringという型を取得
from geometry_msgs.msg import Twist	#速度コマンドをもつ
from datetime import datetime
sim_mode = False

import os
import time

class msg2action():
    def __init__(self):
        self.msg2action_init()

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