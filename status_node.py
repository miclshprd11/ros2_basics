import rclpy
from rclpy.node import Node
from hello_ros_interfaces.msg import Status

class StatusNode(Node):
    def __init__(self):
        super().__init__("status_node")
        self.pub = self.create_publisher(Status, "status", 10)
        self.count = 0
        self.timer = self.create_timer(1.0, self.tick)

    def tick(self):
        msg = Status()
        msg.name = "miclshprd"
        msg.count = self.count
        msg.mood = "learning_ros"
        self.pub.publish(msg)
        self.count += 1

def main():
    rclpy.init()
    node = StatusNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

