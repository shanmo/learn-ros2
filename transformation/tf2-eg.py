import rclpy 
from rclpy.node import Node 
from geomtry_msgs.msg import TransformStamped 
from tf2_ros import StaticTransformBroadcaster 

rclpy.init()
node = Node("transform_node")
static_tf_pub = StaticTransformBroadcaster(node)

t = TransformStamped() 
t.header.stamp = node.get_clock().now().to_msg()
# parent frame is B 
t.header.frame_id = 'B'
# child frame is C 
t.child_frame_id = 'C' 
# translation 
t.transform.translation.x = 0.0 
t.transform.translation.y = 0.0 
t.transform.translation.z = 3.0 

