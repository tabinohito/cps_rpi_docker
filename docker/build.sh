IMAGE_TAG=cps_docker
BASE_IMAGE=ros:noetic-ros-core-focal
set -x
sudo docker build --build-arg BASE_IMAGE=$BASE_IMAGE -t $IMAGE_TAG:arm64v8 .
