import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import TransformStamped 
from tf2_ros import StaticTransformBroadcaster 

rclpy.init()
node = Node("transform_node2")
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
# rotation 
t.transform.rotation.x = 1.0 
t.transform.rotation.y = 0.0 
t.transform.rotation.z = 0.0 
t.transform.rotation.w = 0.0 

static_tf_pub.sendTransform(t)
# use ros2 run tf2_ros tf2_echo B C to listen 

rclpy.spin(node)