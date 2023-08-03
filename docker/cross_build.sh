IMAGE_TAG=cps_docker
AMD64_BASE_IMAGE=ros:noetic-ros-core-focal
ARM64_BASE_IMAGE=ros@sha256:7ff2832f5f3e621f73dbcd5a6e456fff5357b32bf2fd4b34b4e787a916a64699
set -x
sudo docker build --build-arg BASE_IMAGE=$ARM64_BASE_IMAGE -t $IMAGE_TAG:arm64v8  .
sudo docker build --build-arg BASE_IMAGE=$AMD64_BASE_IMAGE -t $IMAGE_TAG:amd64  .
