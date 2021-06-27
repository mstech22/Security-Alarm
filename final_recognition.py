#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import webbrowser
import os
import requests
import time 
from time import sleep 
from sinchsms import SinchSMS
#import socket


face_classifier = cv2.CascadeClassifier('E:/haarcascade_frontalface_default.xml')

def face_detector(size=0.5):
    
    # Convert image to grayscale
    myurl=requests.get('http://192.168.43.1:8080/shot.jpg')
    mypage=myurl.content
    
    byte_array=bytearray(mypage)
    image_1D=np.array(byte_array)
    img=cv2.imdecode(image_1D,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


def sendSMS(): 

	# enter all the details 
	# get app_key and app_secret by registering 
	# a app on sinchSMS 
	number = '+911234567890'
	app_secret = 'jE8s23CZz0+qweBvSAm5Bw=='
	app_key = '142deeeb-62a5-4786-b7f0-0c723f61dde1'

	# enter the message to be sent 
	message = 'Emergency ! M is in Danger !'

	client = SinchSMS(app_key, app_secret) 
	print("Sending '%s' to %s" % (message, number)) 

	response = client.send_message(number, message) 
	message_id = response['messageId'] 
	response = client.check_status(message_id) 

	# keep trying unless the status retured is Successful 
	while response['status'] != 'Successful': 
		print(response['status']) 
		time.sleep(1) 
		response = client.check_status(message_id) 

	print(response['status'])
    
def socketP():
    #s=socket.socket()
    #s=connect(("192.168.43.69",9001))
    s.send("on".encode())
    print("Hellllllllllooooooooooooooooooooo")
    #s.send("off".encode())
    


# Open Webcam
#cap = cv2.VideoCapture(0)

while True:

    #ret, frame = cap.read()
    
    #image, face = face_detector(frame)
    image,face=face_detector()
    image = cv2.resize(image,(640,480))
    
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        results1 = model1.predict(face)
        
        print(results1)
        if results1[1] < 500:
            confidence1 = int( 100 * (1 - (results1[1])/400) )
            display_string1 = str(confidence1) + '% Confident it is User'
            
            #cv2.putText(image, display_string1, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        
        results2 = model2.predict(face)
        print(results2)
        if results2[1] < 500:
            confidence2 = int( 100 * (1 - (results2[1])/400) )
            display_string2 = str(confidence2) + '% Confident it is User'
            
            #cv2.putText(image, display_string2, (100, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        results3 = model3.predict(face)
        x=0
        y=0
        z=0
        w=0
        print(results3)
        if results3[1] < 500:
            confidence3 = int( 100 * (1 - (results3[1])/400) )
            display_string3 = str(confidence3) + '% Confident it is User'
            
            #cv2.putText(image, display_string3, (100, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        results4 = model4.predict(face)
        print(results4)
        if results4[1] < 500:
            confidence4 = int( 100 * (1 - (results4[1])/400) )
            display_string4 = str(confidence4) + '% Confident it is User'
             
            #cv2.putText(image, display_string4, (100, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
        
        if confidence1 > 85:
            cv2.putText(image, "You r T", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            
            x=1
            
            #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://192.168.43.121:8888/notebooks/logistic%20regression%20for%20startup%20sucess%20prediction.ipynb')
           
        if confidence2 > 85:
            cv2.putText(image, "You r J", (250, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            y=1
           # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://192.168.43.121:8888/notebooks/logistic%20regression%20for%20startup%20sucess%20prediction.ipynb')
           
        if confidence3 > 85:
            cv2.putText(image, "you r G", (250, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
            
            z=1
            #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://192.168.43.121:8888/notebooks/logistic%20regression%20for%20startup%20sucess%20prediction.ipynb')
           
        if confidence4 > 85:
            cv2.putText(image, "you r M", (250, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Recognition', image )
        
            w=1
           # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://192.168.43.121:8888/notebooks/logistic%20regression%20for%20startup%20sucess%20prediction.ipynb')
        if(x==0 and y==0 and z==0 and w==1):
            print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            #socketP()
            sendSMS()
        if (x==0 and y==0 and z==0 and w==0):
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
            #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://localhost:8888/notebooks/facereco%20(1)%20(1).ipynb')
        if (x==1 and w==1):
            print("Both Detected....................................DDDDDDDDDDDDDEEEEEEEEEEETTTTTTTTTE")
    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass
        
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
#if x == 1:
#cap.release()
cv2.destroyAllWindows() 
   # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('http://localhost:8888/notebooks/Desktop/logistic%20regression%20for%20startup%20sucess%20prediction.ipynb')
           

