import rclpy 
from rclpy.node import Node 
rclpy.init()
node = Node('hello_world') 
node.get_logger().info('Hello world') 
rclpy.spin(node)