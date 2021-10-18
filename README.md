# football-vision
A ball possession tracker for football videos that tracks players who have possession of the ball in real-time.

Detection and Localization:
The Tiny-YOLO object detector has been used in this work to detect people and football (2 classes that are already a part of the COCO dataset on which the Tiny-YOLO was trained). All player localizations are highlightes using a green bounding box. When a player gets possession of the ball, the colour of the bounding box is automatically changed to red in real-time, while maintaining all other player localizations with a green bounding box. Once a playetr loses possession of the ball, the colour of the bounding box of the player is changed back to green. This is repeated to obtain an effective visualization of players who have the ball in their possession and who don't. An effective tool for football game  analysis projects. 

This work uses darkflow for the implementation of Tiny-YOLO. https://github.com/thtrieu/darkflow

COCO weights have been used in this work for the Tiny-YOLO isntance. This, along with the cfg file for building Tiny-YOLO from darkflow can be found here: https://pjreddie.com/darknet/yolo/

