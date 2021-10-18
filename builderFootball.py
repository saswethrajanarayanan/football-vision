import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

#config InlineBackend.figure_format = 'svg'

options = {'model': 'cfg/yolov2-tiny.cfg',
           'load': 'yolov2-tiny.weights',
           'threshold': 0.5}

tfnet = TFNet(options)

cap = cv2.VideoCapture('messi.mp4')
#image = cv2.imread("clip2.jpg")
ret = True
x_col = 0
valid = ['sports ball', 'person']
#ret, image = cap.read()
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#ret, image = cap.read()
#result = tfnet.return_predict(image)
i = 0
valid = ['sports ball', 'person']
x_col = 0
w_col = 0
h_col = 0

while cv2.waitKey(1) < 0:
    ret, image = cap.read()
    result = tfnet.return_predict(image)
    for i in range(len(result)):
        if result[i]['label'] == 'sports ball':
            x_col = result[i]['topleft']['x']
            w_col = result[i]['bottomright']['x']
            y_col = result[i]['topleft']['y']
            h_col = result[i]['bottomright']['y']
    for i in range(len(result)):
        x, y, w, h = (result[i]['topleft']['x']), (result[i]['topleft']['y']), (result[i]['bottomright']['x']), (
        result[i]['bottomright']['y'])
        label = result[i]['label']
        if label not in valid:
            continue
        if label != 'sports ball':
            if x_col == 0 or w_col == 0:
                image = cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 7)
                image = cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            if x_col - w < 100 or w_col - x < 100:
                if y_col - h < 40 or y - h_col < 40:
                    image = cv2.rectangle(image, (x, y), (w, h), (0, 0, 255), 7)
                    image = cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                else:
                    image = cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 7)
                    image = cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            else:
                image = cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 7)
                image = cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            continue
        label = 'football'
        image = cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 7)
        image = cv2.putText(image, label, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow('Football AI', image)











