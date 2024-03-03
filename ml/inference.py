#Importing Libraries
import torch
from pyzbar.pyzbar import decode
from PIL import Image


# Scan Barcode
def scan_barcode(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Decode all barcodes/QR codes in the image
    decoded_objects = decode(image)
    
    # If no objects found, print that no QR/Barcodes were found
    if not decoded_objects:
        print("No QR/Barcodes found.")
        return
    
    # Print the type and data of each barcode/QR code found
    for obj in decoded_objects:

        data = obj.data.decode('utf-8')

        print(f"Type: {obj.type}")
        print(f"Data: {data}\n")

    return data


def model_predict(img):

    # Load Custom Trained Model
    model = torch.hub.load('../yolov5', 'custom', path='../yolov5/runs/train/exp8/weights/best.pt', source='local', force_reload=True)

    # Make Main Prediction
    model_output = model.predict(img, confidence=60, overlap=60)

    # Find Barcode
    barcode_num = scan_barcode(img)

    # Calculate Scores
    score = 0
    points = {'redbull':50}
    for prediction in model_predictions['predictions']:
        score += points[prediction['class']]

    print("Your Current Score = ",score)






