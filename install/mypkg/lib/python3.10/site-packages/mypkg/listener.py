import rclpy
from  rclpy.node import Node
from  std_msgs.msg import Int16

def cd(msg):
    global node
    node.get_longger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("Listenner")
pub = node.create_publisher(Int16, "countup", cd,  10)
rclpy.spin(node)

