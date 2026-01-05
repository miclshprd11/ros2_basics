import rclpy
from rclpy.node import Node
from hello_ros_interfaces.msg import Status

class MonitorNode(Node):
    def __init__(self):
        super().__init__("monitor_node")
        self.create_subscription(Status, "status", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(
            f"{msg.name} | {msg.count} | {msg.mood}"
        )

def main():
    rclpy.init()
    node = MonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
