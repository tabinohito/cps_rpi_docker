#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def control(msg, twist_pub):#joy to twist
    print(msg)
    L_horizontal = msg.axes[0]  #左ジョイスティック（左右）
    L_vertical = msg.axes[1]    #左ジョイスティック（上下）
    circle = msg.buttons[1]
    velocity = [L_horizontal*(1+circle), L_vertical*(1+circle)]

    t = Twist() #Twistのインスタンスを生成

    t.angular.z, t.linear.x = velocity #twistにjoyから取得したデータを当てはめる

    twist_pub.publish(t)    #twistを配信

if __name__ == '__main__':
    #ノードの初期化
    rospy.init_node('joy_to_twist')
    #配信準備
    twist_pub = rospy.Publisher('/joy/cmd_vel', Twist, queue_size=1)
    #購読
    rospy.Subscriber('/joy', Joy, control, twist_pub)

    rospy.spin()