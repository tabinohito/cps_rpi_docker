#!/bin/bash
SUDO=""
STRING=`groups|grep docker`
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

set -x
$SUDO docker build --build-arg BASE_IMAGE=ros:noetic-ros-base -t irsl_system:arm64 -f Dockerfile.choreonoid_build .
$SUDO docker build --build-arg BASE_IMAGE=irsl_system:arm64 -t cps_docker -f Dockerfile.add_robot_lib .
