#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
HOST_IP=`ip addr show dev docker0 |  grep -Eo 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' |  grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'`
MASTER_IP=${MASTER_IP:-"$HOST_IP"}
IMAGE_NAME=cps_docker_wheel:latest 
CONTAINER_NAME=cps_docker_wheel_container
SERIAL_DEVICE=${SERIAL_DEVICE:-"/dev/ttyUSB0"}
SERIAL_DEVICE_SETTINGS="--device=${SERIAL_DEVICE}:${SERIAL_DEVICE}"
WORK_DIR="/userdir"

VOLUME_SETTING="-v $SCRIPT_DIR/../catkin_ws:/catkin_ws -v $SCRIPT_DIR/../homedir:/home/`whoami` -v $SCRIPT_DIR/../userdir:/userdir" 
USER_SETTING="-u `id -u`:`id -g` -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro"
DISPLAY_SETTING="--env="DISPLAY" --env="QT_X11_NO_MITSHM=1" -v /tmp/.X11-unix:/tmp/.X11-unix:rw"
NET_SETTING="--net=host"
WORKDIR_SETTING="-w $WORK_DIR"
ROS_SETTINGS="--env ROS_IP=${HOST_IP} --env ROS_MASTER_URI=http://${MASTER_IP}:11311"

BUS_ID='1'
GPIO_DEVICE_SETTINGS="--device /dev/gpiomem --device /dev/i2c-$BUS_ID --privileged"

SUDO=""
STRING=`groups|grep docker`
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

set -x
$SUDO docker run -it --rm ${SERIAL_DEVICE_SETTINGS} ${GPIO_DEVICE_SETTINGS} ${USER_SETTING} ${VOLUME_SETTING} ${DISPLAY_SETTING} ${NET_SETTING} ${ROS_SETTINGS} ${WORKDIR_SETTING} --name ${CONTAINER_NAME} ${IMAGE_NAME} bash
