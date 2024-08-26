# urdf_tutorial_ros2

## ROS2 foxy urdf_tutorial 입니다. (교재 참조)

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


## 튜토리얼에 따라 실습 진행



## check URDF

check_urdf 05-visual.urdf

ros2 run xacro xacro 08-macroed.urdf.xacro > 08-macroed.urdf

check_urdf 08-macroed.urdf



