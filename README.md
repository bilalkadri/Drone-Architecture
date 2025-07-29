# Drone-Architecture
This GitHub repository has been developed for the journal paper titled "Enhancing Drone Autonomy through Cloud Integration: A Comprehensive Software Architecture for Navigation, Visual Servoing, and Control"


# ROS1_bridge_installation
# We assume that you have Ubuntu 20 and ROS Noetic installed

# Make sure the below two lines are NOT included in .bashrc
source /opt/ros/noetic/setup.bash
source /opt/ros/foxy/setup.bash


# Add the ROS 2 apt repository
sudo apt update && sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# Install ROS 2 Foxy
sudo apt update
sudo apt install ros-foxy-desktop
source /opt/ros/foxy/setup.bash

# Install ROS1 bridge
sudo apt update
sudo apt install ros-foxy-ros1-bridge



cd
mkdir mavros_bridge_ws
cd mavros_bridge_ws
mkdir src
# we need to git clone the mavros_bridge package now
git clone mavros_bridge_package
sudo apt install ros-foxy-geographic-msgs
cd ..
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select mavros_bridge_listener
source install/setup.bash
# close this terminal


# Terminal 1
source /opt/ros/noetic/setup.bash
roslaunch mbk_ardupilot_drone Complete_Arducopter_Launcher_Water_Tracking_MBK.launch

# Terminal 2
source /opt/ros/noetic/setup.bash
roslaunch mbk_ardupilot_drone Mission_02_Waypoint_Tracking_Arducopter_MBK.launch 


#Terminal 3
source /opt/ros/foxy/setup.bash
export ROS_MASTER_URI=http://localhost:11311
ros2 run ros1_bridge dynamic_bridge

#Terminal 4
source /opt/ros/foxy/setup.bash
cd ~/mavros_bridge_ws

[![DOI](https://zenodo.org/badge/1027278697.svg)](https://doi.org/10.5281/zenodo.16575403)
source install/setup.bash
ros2 run mavros_bridge_listener mavros_subscriber

#Terminal 4
source /opt/ros/foxy/setup.bash
ros2 topic list
