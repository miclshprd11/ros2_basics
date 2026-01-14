This project implements a modular ROS 2 system demonstrating core concepts such as nodes, topics, custom messages, launch files, TF, and RViz visualization. The system follows ROS2 architecture.
The workspace contains an interfaces package that defines a custom Status message used as a shared data contract, and a system package that implements multiple ROS nodes. 
These nodes communicate through topics, with one node publishing system state, another monitoring that state, and a visualization node publishing markers for graphical inspection in RViz.
A launch file is used to bring up the entire system with a single command. 
RViz is used as a debugging and visualization tool, relying on TF and marker topics to display live system behavior.
Although simple in functionality, the project demonstrates correct ROS 2 design patterns and visualization practices that scale directly to real robotic applications such as navigation,
perception, and hardware integration.
