#!/usr/bin/env python3 
import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String, UInt32 

class WriterNode(Node): 
    def __init__(self, name): 
        super().__init__(name)
        self.get_logger().info(f"hi, I am {name}, I am a blogger")
        self.pub_blog = self.create_publisher(String, "blog", 10)

        self.i = 0 
        timer_period = 5 
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.account = 80 
        self.submoney = self.create_subscription(UInt32, "blog_money", self.receive_callback, 10)

    def timer_callback(self): 
        msg = String()
        msg.data = f"blog {self.i}: sherlock holmes meets moriaty for the {self.i}th time"
        self.pub_blog.publish(msg)
        self.get_logger().info(f"Watson: I published blog: {msg.data}")
        self.i += 1 

    def receive_callback(self, money): 
        self.account += money.data 
        self.get_logger().info(f"Watson: I received {self.account} pound")

def main(args=None): 
    rclpy.init(args=args)
    node = WriterNode("watson")
    rclpy.spin(node)
    rclpy.shutdown()

