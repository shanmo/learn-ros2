import numpy as np 
import math 

a = np.asarray([1.0, 1.0, 1.0]).reshape(3, 1)

theta = math.radians(45)
bRa = np.asarray([math.cos(theta), -math.sin(theta), 0,
                  math.sin(theta), math.cos(theta), 0,
                  0, 0, 1]).reshape(3, 3)

b = bRa @ a 
print(f"b is {b.T}")

theta = math.radians(180)
bRc = np.asarray([1, 0, 0,
                0, math.cos(theta), -math.sin(theta),
                0, math.sin(theta), math.cos(theta)]).reshape(3, 3)
cRp = np.eye(3)
bRp = bRc @ cRp

bPc = np.asarray([0, 0, 3]).reshape(3, 1)
cPp = np.asarray([2, 1, 2]).reshape(3, 1) 
bPp = bRc @ cPp + bPc
print(f"bPp is {bPp.T}")

# the above is equivalent to 

# ros2 run tf2_ros static_transform_publisher 0 0 3 0 0 3.14 B C
# ros2 run tf2_ros static_transform_publisher 2 1 2 0 0 0 C P

# ros2 run tf2_ros tf2_echo B P
# - Translation: [2.000, -1.003, 1.002]
# - Rotation: in Quaternion [1.000, 0.000, 0.000, 0.001]
