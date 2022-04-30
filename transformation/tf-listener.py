import rclpy 
from rclpy.node import Node 

from tf2_ros import TransformException 
from tf2_ros.buffer import Buffer 
from tf2_ros.transform_listener import TransformListener 

rclpy.init()
node = Node("transform_node3")

tf_buffer = Buffer()
tf_listener = TransformListener(tf_buffer, node)

def transform_callback(): 
    try: 
        now = rclpy.time.Time()
        trans = tf_buffer.lookup_transform('B', 'P', now)
        print(f"trans {trans}")
    except TransformException as ex:
        print(f"could not get transform from P to B: {ex}") 
