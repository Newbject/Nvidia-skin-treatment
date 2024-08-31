#!/usr/bin/python3

import jetson_inference
import jetson_utils

import argparse

# parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
#parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect.")
args = parser.parse_args()

# load an image (into shared CPU/GPU memory)
img = jetson_utils.loadImage(args.filename)

# load the recognition network
net = jetson_inference.imageNet(model="Skin_Conditions.onnx", labels="labels.txt", input_blob="input_0", output_blob="output_0")

# classify the image
class_idx, confidence = net.Classify(img)

# find the object description
class_desc = net.GetClassDesc(class_idx)

# print out the result
#print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))

def sentence(skin_condition, link, confidence):
    print("with a confidence of " + str(confidence) + ", these are some treatments for " +  skin_condition)
    print(link)

if class_idx == 0:
    print("It seems like you have Acne", end = " ")
    sentence(class_desc, "https://www.mayoclinic.org/diseases-conditions/acne/diagnosis-treatment/drc-20368048", confidence * 100)

elif class_idx == 1:
    print("It seems like you have Rosacea", end = " ")
    sentence(class_desc, "https://www.mayoclinic.org/diseases-conditions/rosacea/diagnosis-treatment/drc-20353820", confidence * 100)

elif class_idx == 2:
    print("It seems like you have Milia", end = " ")
    sentence(class_desc, "https://my.clevelandclinic.org/health/diseases/17868-milia", confidence * 100)

elif class_idx == 3:
    print("It seems like you have Keratosis", end = " ")
    sentence(class_desc, "https://www.mayoclinic.org/diseases-conditions/keratosis-pilaris/diagnosis-treatment/drc-20351152", confidence * 100)

elif class_idx == 4:
    print("It seems like you have Eczema", end = " ")
    sentence(class_desc, "https://www.mayoclinic.org/diseases-conditions/atopic-dermatitis-eczema/diagnosis-treatment/drc-20353279", confidence * 100)

elif class_idx == 5:
    print("It seems like you have Carcinoma", end = " ")
    sentence(class_desc, "https://www.mayoclinic.org/diseases-conditions/squamous-cell-carcinoma/diagnosis-treatment/drc-20352486")
