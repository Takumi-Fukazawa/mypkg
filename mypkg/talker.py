# SPDX-FileCopyrightText: 2022 Takumi Fukazawa
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from  rclpy.node import Node
from  person_msgs.msg import Person

class Talker():
    def __init__(self,node):
        self.pub = node.create_publisher(Person, "person", 10)
        self.n = 1
        node.create_timer(0.5, self.cb)
                                                                    
    def cb(self):
        msg = Person()
        msg.message = input("文字列を入力してください ")
        msg.log = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)
         
if __name__ == '__main__':
    main()





