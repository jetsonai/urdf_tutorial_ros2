# urdf_tutorial_ros2

ros2 foxy urdf_tutorial

## dependency 설치

sudo apt install ros-foxy-joint-state-publisher

sudo apt install ros-foxy-joint-state-publisher-gui

## urdf tutorial workspace 

mkdir -p urdf_ws/src

cd urdf_ws/src

## urdf tutorial package

git clone https://github.com/jetsonai/urdf_tutorial_ros2 

cd ..

colcon build --symlink-install

source ./install/setup.bash

ros2 launch urdf_tutorial_ros2 display_urdf.launch.py 

