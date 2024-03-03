#Importing Libraries
import torch
from pyzbar.pyzbar import decode
from PIL import Image
import argparse
import json

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
    model_output = model(img)

    results_json = model_output.pandas().xyxy[0].to_json(orient="records")
    model_predictions = json.loads(results_json)

    # Predictions and Save Output
    #model_predictions = model_output.json()
    #model_output.save("../images/prediction.jpg")

    # Calculate Scores
    score = 0
    points = {'redbull':50}
    for prediction in model_predictions:
        score += points[prediction['name']]

    print("Your Current Score = ",score)

    # # Find Barcode
    # barcode_num = scan_barcode(img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Predictions')
    parser.add_argument('img', type=str, help='Send image path to make predictions')
    
    args = parser.parse_args()

    model_predict(args.img)



