#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def control(msg, twist_pub):#joy to twist
    print(msg)
    R_horizontal = msg.axes[3]  #右ジョイスティック（左右）
    L_vertical = msg.axes[1]*0.5    #左ジョイスティック（上下）
    L_horizontal = msg.axes[0]*0.5  #左ジョイスティック（左右）

    circle = msg.buttons[1]
    velocity = [R_horizontal*(1+circle), L_vertical*(1+circle), L_horizontal*(1+circle)]

    t = Twist() #Twistのインスタンスを生成

    t.angular.z, t.linear.x , t.linear.y = velocity #twistにjoyから取得したデータを当てはめる

    twist_pub.publish(t)    #twistを配信

if __name__ == '__main__':
    #ノードの初期化
    rospy.init_node('joy_to_twist')
    #配信準備
    twist_pub = rospy.Publisher('/joy/cmd_vel', Twist, queue_size=1)
    #購読
    rospy.Subscriber('/joy', Joy, control, twist_pub)

    rospy.spin()