#!/bin/bash

CONTAINER_NAME=cps_docker_container
SUDO=""
STRING=`groups|grep docker`
if [ -z "$STRING" ]; then
  SUDO="sudo "
fi

${SUDO} docker exec -it ${CONTAINER_NAME} bash