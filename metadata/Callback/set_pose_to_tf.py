from geometry_msgs.msg import TransformStamped
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
import rospy
import sys
import time

# Wait for a bit?
time.sleep(5)

stat_br = StaticTransformBroadcaster()
t = TransformStamped()
t.header.frame_id = "map"
t.child_frame_id = "odom"

# Translation
t.transform.translation = msg.pose.pose.position

# Quaternion Rotation
t.transform.rotation = msg.pose.pose.orientation

# Send
stat_br.sendTransform(t)