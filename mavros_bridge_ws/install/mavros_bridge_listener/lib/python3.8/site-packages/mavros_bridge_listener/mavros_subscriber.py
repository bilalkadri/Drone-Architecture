import rclpy
from rclpy.node import Node

from sensor_msgs.msg import NavSatFix, Image, Imu, MagneticField, BatteryState
from geometry_msgs.msg import TwistStamped, PoseStamped, Point, Twist
from std_msgs.msg import Float32MultiArray



class MavrosSubscriber(Node):
    def __init__(self):
        super().__init__('mavros_subscriber')

        # Subscriptions to MAVROS + ROS1 topics that use standard messages
        self.create_subscription(NavSatFix, '/mavros/global_position/global', self.gps_callback, 10)
        self.create_subscription(PoseStamped, '/mavros/local_position/pose', self.pose_callback, 10)
        self.create_subscription(Image, '/webcam/image_raw', self.image_callback, 10)
        self.create_subscription(Float32MultiArray, '/Water_Reservoir_Location_Topic', self.reservoir_callback, 10)
        self.create_subscription(Float32MultiArray, '/Water_Discharge_Location_Topic', self.discharge_callback, 10)
        self.create_subscription(TwistStamped, '/mavros/setpoint_velocity/cmd_vel', self.cmd_vel_callback, 10)
        self.create_subscription(Imu, '/mavros/imu/data', self.imu_callback, 10)
        self.create_subscription(MagneticField, '/mavros/imu/mag', self.mag_callback, 10)
        self.create_subscription(BatteryState, '/mavros/battery', self.battery_callback, 10)

        self.get_logger().info('Subscribed to MAVROS and compatible ROS1 topics.')

    # Callbacks
    def gps_callback(self, msg: NavSatFix):
        self.get_logger().info(f"[GPS] Lat: {msg.latitude:.6f}, Lon: {msg.longitude:.6f}, Alt: {msg.altitude:.2f}")

    def pose_callback(self, msg: PoseStamped):
        pos = msg.pose.position
        self.get_logger().info(f"[Local Pose] x={pos.x:.2f}, y={pos.y:.2f}, z={pos.z:.2f}")

    def image_callback(self, msg: Image):
        self.get_logger().info(f"[Image] {msg.width}x{msg.height}, encoding={msg.encoding}")

    def reservoir_callback(self, msg: Float32MultiArray):
        data_str = ', '.join([f"{x:.2f}" for x in msg.data])
        self.get_logger().info(f"[Reservoir Location] Data: [{data_str}]")

    def discharge_callback(self, msg: Float32MultiArray):
       data_str = ', '.join([f"{x:.2f}" for x in msg.data])
       self.get_logger().info(f"[Discharge Location] Data: [{data_str}]")


    def cmd_vel_callback(self, msg: TwistStamped):
        lin = msg.twist.linear
        ang = msg.twist.angular
        self.get_logger().info(
            f"[Setpoint Velocity] Linear: x={lin.x:.2f}, y={lin.y:.2f}, z={lin.z:.2f} | "
            f"Angular: x={ang.x:.2f}, y={ang.y:.2f}, z={ang.z:.2f}"
    )


    def imu_callback(self, msg: Imu):
        self.get_logger().info(f"[IMU] Orientation: x={msg.orientation.x:.2f}, y={msg.orientation.y:.2f}, z={msg.orientation.z:.2f}")

    def mag_callback(self, msg: MagneticField):
        self.get_logger().info(f"[Magnetometer] x={msg.magnetic_field.x:.2f}, y={msg.magnetic_field.y:.2f}, z={msg.magnetic_field.z:.2f}")

    def battery_callback(self, msg: BatteryState):
        self.get_logger().info(f"[Battery] Voltage: {msg.voltage:.2f}V, Current: {msg.current:.2f}A, %: {msg.percentage:.0%}")

def main(args=None):
    rclpy.init(args=args)
    node = MavrosSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
