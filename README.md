# Boat Detection System

I built this as my first computer vision project to learn how AI can detect 
objects in real life. The system can find boats in images and videos by drawing 
boxes around them.

## Why I built this
I wanted to understand how surveillance systems work in real life like port 
monitoring and coastal security. So I built a small version of it myself 
using free tools.

## What it can do
1.Give it any boat image and it will draw a box around the boat
2.Give it a video and it will detect boats in every frame
3.Shows how confident it is (like 93% sure its a boat)
4.Counts how many boats are found

## Tools I used
1.Python - main programming language
2.YOLOv8 - the AI model that actually detects boats
3.OpenCV - reads images and videos, draws the boxes
4.COCO Dataset - what YOLO was trained on, already includes boats

## How to run it yourself

Install the required libraries first:
pip install ultralytics opencv-python

To detect boats in an image:
python detect_image.py

To detect boats in a video:
python detect_video.py

## What I learned
1.How AI object detection works
2.How to use a pre trained model without training from scratch
3.How videos are just a collection of images processed frame by frame
4.How to connect different libraries together in Python

## Challenges I faced
1.Setting up the correct file paths on Windows
2.Fixing corrupted video files so OpenCV could read them
3.Understanding what confidence scores mean

## Author
Advita-Computer Science Student
This is one of my first Python projects and I am proud of it!
