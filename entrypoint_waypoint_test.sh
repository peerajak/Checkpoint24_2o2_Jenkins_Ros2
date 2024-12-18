#! /bin/bash 

source /opt/ros/galactic/setup.bash
source /ros2_ws/install/setup.bash 
sleep 3
ros2 launch tortoisebot_bringup bringup.launch.py use_sim_time:=True &
sleep 7
cd /ros2_ws && colcon build
cd /ros2_ws && colcon test --packages-select tortoisebot_waypoints --event-handler=console_direct+


