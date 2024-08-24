
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time")

    pkg_path = os.path.join(get_package_share_directory("urdf_tutorial_ros2"))
    #xacro_file = os.path.join(pkg_path, "urdf", "01-myfirst.urdf")
    #xacro_file = os.path.join(pkg_path, "urdf", "02-multipleshapes.urdf")
    #xacro_file = os.path.join(pkg_path, "urdf", "03-origins.urdf")
    #xacro_file = os.path.join(pkg_path, "urdf", "04-materials.urdf")
    #xacro_file = os.path.join(pkg_path, "urdf", "05-visual.urdf")
    #xacro_file = os.path.join(pkg_path, "urdf", "06-flexible.urdf")
    xacro_file = os.path.join(pkg_path, "urdf", "07-physics.urdf")
    robot_description = xacro.process_file(xacro_file)
    params = {"robot_description": robot_description.toxml(), "use_sim_time": use_sim_time}

    rviz_config_dir = os.path.join( pkg_path, 'rviz','model.rviz')
        
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "use_sim_time", default_value="false", description="use sim time"
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                parameters=[params],
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                output="screen",
                parameters=[params],
            ),            
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', rviz_config_dir],
                output='screen'
            ),            
        ]
    )
