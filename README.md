# Nvidia AI Skin Disease Detection

 This project is meant for quick detection of skin diseases (Acne, Carcinoma, Eczema, Keratosis, Milia, Rosacea) and giving a link on how to treat it. This program can be helpful in many cases. for example, when it's midnight and you find a part of your skin red, rather than gping to the doctor right away, this AI can help identify the type of skin disease you have and give you ways to treat it.

![Eczema_2](https://github.com/user-attachments/assets/49bdeb2c-b163-44f0-b30d-90d075a832b6)

![Eczema Terminal](https://github.com/user-attachments/assets/6d7afb26-8723-41d6-a1ce-469f0829f4c1)


## The Algorithm

This system was trained using a New Network. 

The strategies I used to train the model were resNet-18, Onnx and Imagenet.

Firstly, I found a dataset and formatted into a way that could be used for training.

I changed the network to Skin_Conditions.ONNX to store the neural network, then made an output folder for future storing.

I also created a custom code to lead the user into a reputable website explaining treatments for the types of skin diseases.

## Running this project

1. Select a test image from the 6 classes

2. Run "Python3 final_code.py testImagePath" in the terminal

3. Get the results!

## Demonstration Video

[(https://drive.google.com/file/d/1mtZ4ysrEsEByPBJMc4pYy31tb6b2UcU4/view?usp=sharing)](https://drive.google.com/file/d/1mtZ4ysrEsEByPBJMc4pYy31tb6b2UcU4/view?usp=sharing)
