import rclpy 
from rclpy.node import Node 

def main(args=None): 
    rclpy.init(args=args)
    node = Node("watson")
    node.get_logger().info("hi, I am John Watson")
    rclpy.spin(node)
    rclpy.shutdown()

