#!/usr/bin/env python

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self,topic):
    self.image_pub = rospy.Publisher(topic+'/face',Image, queue_size=2)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(topic,Image,self.callback, queue_size=2)


  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    crackCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cv_image =cv2.flip(cv_image,-1)
    cracks = crackCascade.detectMultiScale(cv_image,scaleFactor=1.1,minNeighbors=5,minSize=(100, 100),flags = 0)
    if(len(cracks)):
		for (x, y, w, h) in cracks:
			cv2.rectangle(cv_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
   # gray_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
   # haar_face = gray_image[0:300, 0:220]
    
    #cv2.imshow("Face Detection", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

def main(args):
  rospy.init_node('tx2_ros_face_detection', anonymous=True)

  topic = '/csi_cam/image_raw' #change zed_topic here

  img = image_converter(topic)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

