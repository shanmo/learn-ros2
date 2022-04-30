import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import TransformStamped 
from tf2_ros import TransformBroadcaster 

rclpy.init()
node = Node("transform_node1")
tf_pub = TransformBroadcaster(node)

t = TransformStamped() 
# parent frame is C 
t.header.frame_id = 'C'
# child frame is P
t.child_frame_id = 'P' 
# translation 
t.transform.translation.x = 2.0 
t.transform.translation.y = 1.0 
t.transform.translation.z = 2.0 
# rotation 
t.transform.rotation.x = 1.0 
t.transform.rotation.y = 0.0 
t.transform.rotation.z = 0.0 
t.transform.rotation.w = 0.0 

def send_transform(): 
    t.header.stamp = node.get_clock().now().to_msg()
    tf_pub.sendTransform(t) 

node.create_timer(0.1, send_transform)
rclpy.spin(node)