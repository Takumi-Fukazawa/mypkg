# SPDX-FileCopyrightText: 2022 Takumi Fukazawa
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from  rclpy.node import Node
from  person_msgs.msg import Person
import random
import string
class Talker():
    def __init__(self,node):
        self.pub = node.create_publisher(Person, "person", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)
                                                                    
    def cb(self):
        msg = Person()
        string_seed = string.digits + string.ascii_lowercase + string.ascii_uppercase
        random_string_list = random.choices(string_seed, k=10)
        msg.message = ''.join(random_string_list)
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





