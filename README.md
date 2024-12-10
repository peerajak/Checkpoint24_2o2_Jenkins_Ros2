# Checkpoint24_2o2_Jenkins_Ros2

### How to solve this checkpoint
- Done build docker that could test the tortoisebot_waypoints
- Jenkins
    - Create a Jenkins pipeline for automating the test process
    - Automate the test process on each Git push, pull request

## Build and run dockers manually

In this section, more details about how to build an run docker is written.

build docker 

```
docker build -t tortoisebot-waypoints-ros2-test:v1 .
```

- Running on the construct's computer

```
docker context use default
xhost +local:root
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix tortoisebot-waypoints-ros2-test:v1 
```
- Running on my Local computer

```
docker context use default
xhost +local:root
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --gpus all --net=host tortoisebot-waypoints-ros2-test:v1 
```

