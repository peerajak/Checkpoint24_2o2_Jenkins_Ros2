import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
from launch_ros.actions import Node
import os
from launch.actions import DeclareLaunchArgument, ExecuteProcess, LogInfo, RegisterEventHandler, TimerAction
from launch.event_handlers import OnProcessStart

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='tortoisebot_gazebo').find('tortoisebot_gazebo')
    world_path=os.path.join(pkg_share, 'worlds/room2.sdf'),
    use_sim_time = LaunchConfiguration('use_sim_time')
    spawn_world = ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 
                                            'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so',world_path], 
                                            output='screen')
    spawn_entity = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'tortoisebot', '-topic', 'robot_description'],
            parameters= [{'use_sim_time': use_sim_time}],
            output='screen')

    return launch.LaunchDescription([
        spawn_world,
        DeclareLaunchArgument(name='use_sim_time', default_value='False',
                                description='Flag to enable use_sim_time'),
        RegisterEventHandler(
            OnProcessStart(
                target_action=spawn_world,
                on_start=[
                    LogInfo(msg='Spawn world finished'),                   
                    TimerAction(
                        period=2.0,
                        actions=[spawn_entity],
                    )
                ]
            )
        )
    ])
    
