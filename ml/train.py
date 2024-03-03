# To Train Custom Model
import torch
from ultralytics import YOLO
from roboflow import Roboflow

# Download the dataset
rf = Roboflow(api_key="API KEY")
project = rf.workspace("uottahack").project("sustain")
version = project.version(3)
dataset = version.download("yolov8-obb")

# Run training script from Yolov5
import subprocess

# Define the command you want to run as a string:
command = "python ../yolov5/train.py --img 640 --epochs 100 --data Sustain-1/data.yaml --weights yolov5s.pt"

# Use subprocess.run to execute the command:
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)