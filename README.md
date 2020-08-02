# tx2-ros-face-detection

This rospy script is to test the working of  csi camera of TX2 as well as ROS and Opencv Packages.

```
git clone https://github.com/roboticsengineer93/tx2-ros-face-detection.git
cd tx2-ros-face-detection
# Download [haarcascade_frontalface_default.xml]
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
```

ROS node :  tx2_ros_face_detection

Subscribers : /csi_cam/image_raw

Publishers : /csi_cam/image_raw/face 