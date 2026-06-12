from geometry_msgs.msg import TransformStamped
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
import rospy
import sys
import time
from tf import transformations

stat_br = StaticTransformBroadcaster()
t = TransformStamped()
t.header.stamp = rospy.Time.now()
t.header.frame_id = "map"
t.child_frame_id = "odom"

# Translation
t.transform.translation = msg.pose.pose.position
t.transform.translation.z = 0.0
# Quaternion Rotation
orientation_q = msg.pose.pose.orientation
orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
roll, pitch, yaw = transformations.euler_from_quaternion(orientation_list)
orientation_q_new = transformations.quaternion_from_euler(0, 0, yaw)
t.transform.rotation.x = orientation_q_new[0]
t.transform.rotation.y = orientation_q_new[1]
t.transform.rotation.z = orientation_q_new[2]
t.transform.rotation.w = orientation_q_new[3]

# Send
stat_br.sendTransform(t)
# Wait for a bit?
time.sleep(1)
# Send to set_pose_pub
gd.oport['set_pose_pub'].send(msg)