#!/bin/bash
set -e

# setup ros environment
if [ -e "/catkin_ws/devel/setup.bash" ]; then
    source "/catkin_ws/devel/setup.bash" --
elif [  -e "/choreonoid_ws/install/setup.bash"  ]; then
    source "/choreonoid_ws/install/setup.bash" --
else 
    source "/opt/ros/$ROS_DISTRO/setup.bash" --
fi
exec "$@"