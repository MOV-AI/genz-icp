from geometry_msgs.msg import TransformStamped
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
import rospy
import sys
import tf.geometry_msgs

stat_br = StaticTransformBroadcaster()
t = TransformStamped()
t.header.stamp = rospy.Time.now()
t.header.frame_id = "odom"
t.child_frame_id = "map"

# Translation
t.transform.translation = msg.pose.pose.position

# Quaternion Rotation
t.transform.rotation = msg.pose.pose.orientation

# Send
stat_br.sendTransform(t)

# Shutdown
rospy.signal_shutdown("Finished setting pose. Quitting now.")
sys.exit()