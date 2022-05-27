#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 22:53:21 2022

@author: mengzi
"""
import face_recognitin
import os
import  cv2
KNOWN_FACE_DIR="known_faces"
UNKOWN_FACE_DIR="unknown_faces"
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
        result = face_recognition.compare(known_faces,face_encoding,TOLERANCE)
        match = None
        if True in results:
            match = knows_names