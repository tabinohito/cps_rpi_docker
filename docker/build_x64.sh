#!/bin/bash
SUDO=""
STRING=`groups|grep docker`
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

set -x
$SUDO docker pull docker pull repo.irsl.eiiris.tut.ac.jp/irsl_system:noetic
$SUDO docker build --build-arg BASE_IMAGE=repo.irsl.eiiris.tut.ac.jp/irsl_system:noetic -t cps_docker -f Dockerfile.add_robot_lib .