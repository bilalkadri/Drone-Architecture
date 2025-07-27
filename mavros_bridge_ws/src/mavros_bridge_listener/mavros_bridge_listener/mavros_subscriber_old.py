import rclpy
from rclpy.node import Node

from sensor_msgs.msg import NavSatFix, Image
from geometry_msgs.msg import PoseStamped, Point

class MavrosSubscriber(Node):
    def __init__(self):
        super().__init__('mavros_subscriber')

        # Subscribing to all 5 topics
        self.create_subscription(NavSatFix, '/mavros/global_position/global', self.gps_callback, 10)
        self.create_subscription(PoseStamped, '/mavros/local_position/pose', self.pose_callback, 10)
        self.create_subscription(Image, '/webcam/image_raw', self.image_callback, 10)
        self.create_subscription(Point, '/Water_Reservoir_Location_Topic', self.reservoir_callback, 10)
        self.create_subscription(Point, '/Water_Discharge_Location_Topic', self.discharge_callback, 10)

        self.get_logger().info('Subscribed to MAVROS and custom topics.')

    def gps_callback(self, msg: NavSatFix):
        self.get_logger().info(f"[GPS] Lat: {msg.latitude:.6f}, Lon: {msg.longitude:.6f}, Alt: {msg.altitude:.2f}")

    def pose_callback(self, msg: PoseStamped):
        pos = msg.pose.position
        self.get_logger().info(f"[Local Pose] x={pos.x:.2f}, y={pos.y:.2f}, z={pos.z:.2f}")

    def image_callback(self, msg: Image):
        self.get_logger().info(f"[Image] Received image: {msg.width}x{msg.height}, encoding={msg.encoding}")

    def reservoir_callback(self, msg: Point):
        self.get_logger().info(f"[Reservoir Location] x={msg.x:.2f}, y={msg.y:.2f}, z={msg.z:.2f}")

    def discharge_callback(self, msg: Point):
        self.get_logger().info(f"[Discharge Location] x={msg.x:.2f}, y={msg.y:.2f}, z={msg.z:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = MavrosSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
