#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0); pwd)
IMAGE_NAME=cps_docker_wheel:latest
CONTAINER_NAME=cps_docker_sourcebuild
WORK_DIR="/catkin_ws"

VOLUME_SETTING="-v $SCRIPT_DIR/../catkin_ws:/catkin_ws -v $SCRIPT_DIR/../homedir:/home/`whoami`"
USER_SETTING="-u `id -u`:`id -g` -v /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro"
WORKDIR_SETTING="-w $WORK_DIR"

set -x
sudo docker run --rm ${USER_SETTING} ${VOLUME_SETTING} ${WORKDIR_SETTING} --name ${CONTAINER_NAME} ${IMAGE_NAME} bash -c "catkin_make"
