#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 

class WriterNode(Node): 
    def __init__(self, name): 
        super().__init__(name)
        self.get_logger().info(f"hi, I am {name}, I am a blogger")

def main(args=None): 
    rclpy.init(args=args)
    node = WriterNode("watson")
    rclpy.spin(node)
    rclpy.shutdown()

