from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('gazebo_racing_tracks')
    world_path = os.path.join(pkg_share, 'worlds', 'snow_track.sdf')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', '-v', '4', world_path],
            output='screen')
    ])