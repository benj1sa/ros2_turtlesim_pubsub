#!/user/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")

def main(args=None):
    # initialize ros2 communcations
    rclpy.init(args=args)
    
    # nodes go here
    node = MyNode()

    rclpy.shutdown()

if __name__ == '__main__':
    main()