#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 22:53:21 2022

@author: mengzi
"""
#pip install cmake -i https://pypi.tuna.tsinghua.edu.cn/simple
#pip install face_recognition -i https://pypi.tuna.tsinghua.edu.cn/simple
#pip install opencv_python -i https://pypi.tuna.tsinghua.edu.cn/simple
'''
https://stackoverflow.com/questions/51721695/dlib-installation-error
Here is how I solved the same issue.

Make sure you have installed cmake and CMAKE_FOLDER\bin added it in environment varaible
Install anaconda
then run following commands in anaconda shell.
conda update conda

conda update anaconda

create new environment conda create -n env_dlib python=3.6
activate enviroment conda activate env_dlib
install dlib conda install -c conda-forge dlib
Verify your installation in python shell using

import dlib
 dlib.__version__
'''

import face_recognitin
import os
import  cv2
KNOWN_FACES_DIR="known_faces"
UNKNOWN_FACES_DIR="unknown_faces"
TOLERANCE=0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

print("loading known faces")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACE_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image=face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        encoding=face_recognitin.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)

print("processing unknown faces")
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image = face_recognitin.load_image_file(f"{KNOWN_FACES_DIR}/{filename}")
    locations = face_recognition.face_locations(image,model=MODEL)
    encodings = face_recognition.face_encodings(image,lacations)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    
    for face_encoding, face_location in zip(encodings,lacations):
        result = face_recognition.compare_faces(known_faces,face_encoding,TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found:{match}")

            top_left=(face_location[3],face_location[0])
            bottom_right=(face_location[1],face_location[2])

            color=[0,255,0]
            cv2.rectangle(image,top_left,bottom_right,color,FRAME_THICKNESS)


            top_left=(face_location[3],face_location[2])
            bottom_right=(face_location[1],face_location[2]+22)
            cv2.rectangle(image,top_left,bottom_right,color,cv2.FILLED)

            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)
    cv2.imshow(filename,image)
    cv2.waitKey(10000)
    # cv2.destoryWindow(filename)