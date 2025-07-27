import rclpy
from rclpy.node import Node

from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PoseStamped

class MavrosSubscriber(Node):
    def __init__(self):
        super().__init__('mavros_subscriber')

        self.create_subscription(NavSatFix, '/mavros/global_position/global', self.gps_callback, 10)
        self.create_subscription(PoseStamped, '/mavros/local_position/pose', self.pose_callback, 10)

        self.get_logger().info('Subscribed to MAVROS topics.')

    def gps_callback(self, msg):
        self.get_logger().info(f"GPS: Lat {msg.latitude:.6f}, Lon {msg.longitude:.6f}, Alt {msg.altitude:.2f}")

    def pose_callback(self, msg):
        pos = msg.pose.position
        self.get_logger().info(f"Local Pose: x={pos.x:.2f}, y={pos.y:.2f}, z={pos.z:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = MavrosSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
