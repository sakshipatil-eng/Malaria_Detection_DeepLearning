
# 🦠 Malaria Detection Using Deep Learning


##  Project Overview

  This project implements a **Deep Learning based malaria detection system** that classifies microscopic blood cell images as **Parasitized (infected)** or **Uninfected (healthy)**.
A **Convolutional Neural Network (CNN)** model is trained on malaria cell images and integrated with a simple web interface for easy prediction.

 The application allows users to upload a cell image and receive a prediction indicating whether malaria infection is present.



## Purpose of the Project


  This project was developed for **educational and academic purposes** to study the application of deep learning techniques in medical image classification. It demonstrates how convolutional neural networks can be used to analyze microscopic cell images and how a simple web interface can be built to interact with the trained model.



##  Technologies Used 

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* PIL (Python Imaging Library)
* Google Colab



##  Dataset
  
The model was trained using a **Malaria Cell Images Dataset** containing microscopic blood smear images.

The dataset includes two classes:

* **Parasitized** – Malaria infected cells
* **Uninfected** – Healthy cells

These images are used to train a CNN model for binary classification.

 

##  Model Architecture


The deep learning model consists of:

* Image Rescaling Layer
* Convolutional Layers
* MaxPooling Layers
* Flatten Layer
* Dense Fully Connected Layers
* Dropout Layer for regularization
* Sigmoid activation for binary classification

 

##  Web Application


A simple web interface built using **Streamlit** allows users to:

1. Upload a cell image
2. Process the image using the trained model
3. Display the prediction result

The system predicts:

* 🦠 **Parasitized (Malaria Infected)**
* ✅ **Uninfected (Healthy)**



##  Project Structure


malaria-detection

│

├── malaria_detection.ipynb

├── app.py

├── README.md

└── LICENSE




##  Trained Model


The trained model file is large and hosted externally.

Download the model here:

(https://drive.google.com/file/d/1C-vjDReeCKAOITCCCnJ6QAUeTP4B9B5P/view?usp=drive_link)

After downloading, place **malaria_model.h5** inside the project folder before running the application.


##  How to Run the Project


1. Clone the repository

git clone (https://github.com/sakshipatil-eng/Malaria_Detection_DeepLearning.git)


2. Install required libraries


pip install streamlit tensorflow numpy pillow


3. Run the Streamlit application


streamlit run app.py


4. Upload a cell image to test the malaria detection model.



##  Disclaimer


  This project is created for **educational and demonstration purposes only** and should not be used for real medical diagnosis.


## Output

<img width="1915" height="984" alt="Image" src="https://github.com/user-attachments/assets/0ad79208-0131-4ea3-b21a-013a1fea2e4f" />

<img width="1825" height="902" alt="Image" src="https://github.com/user-attachments/assets/8b75d82f-78f9-4ea8-825d-b01ed5d5da6b" />

<img width="1871" height="904" alt="Image" src="https://github.com/user-attachments/assets/136b495c-433c-46f8-ade1-42b22e19b213" />



