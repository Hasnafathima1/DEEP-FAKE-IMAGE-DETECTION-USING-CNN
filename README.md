
# Deepfake Image Detection Using CNN and Flask

## Overview

This project is a Deep Learning based **Deepfake Image Detection System** that classifies images into **Real** and **Fake** categories using a **Convolutional Neural Network (CNN)**.

The trained CNN model is deployed using a **Flask Web Application**, where users can upload an image and get the prediction result with confidence score.

---

## Features

✅ Deepfake image classification using CNN  
✅ Real-time image prediction using Flask  
✅ Image preprocessing and normalization  
✅ Confidence score display  
✅ User-friendly web interface  

---

## Technologies Used

- Python
- TensorFlow / Keras
- CNN (Convolutional Neural Network)
- Flask
- HTML & CSS
- NumPy
- Scikit-learn

---

## Dataset

The model is trained on a deepfake image dataset containing two classes:

- Fake Images
- Real Images

Dataset:

| Type | Images |
|------|--------|
| Training | 7007 |
| Validation | 3000 |

---

## Project Workflow

```
Image Input
     |
     ↓
Image Preprocessing
(Resize 224×224 + Normalize)
     |
     ↓
CNN Model
     |
     ↓
Prediction Probability
     |
     ↓
Real / Fake Classification
     |
     ↓
Display Result using Flask
```

---

## CNN Architecture

```
Input Image
     |
Conv2D (32 filters)
     |
MaxPooling
     |
Conv2D (64 filters)
     |
MaxPooling
     |
Flatten
     |
Dense Layer (128 neurons)
     |
Dropout
     |
Sigmoid Output
     |
Real / Fake Prediction
```

---

## Model Training

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Epochs | 25 |
| Image Size | 224 × 224 |
| Classes | 2 |

---

## Results

| Metric | Value |
|--------|-------|
| Training Accuracy | 74% |
| Validation Accuracy | 73.10% |
| Validation Loss | 0.5282 |

Confusion Matrix:

```
[[1053 447]
 [360 1140]]
```

---

## Flask Application

The Flask application performs:

1. User uploads image.
2. Flask receives the image.
3. Image is resized and normalized.
4. CNN model predicts the class.
5. Real/Fake result and confidence are displayed.

---
## Flask Application Demo


### Home Page

![Flask Home Page](Screenshot 2026-07-01 230337.png)


### Prediction Result

![Prediction Result]("C:\Users\HASNA FATHIMA\OneDrive\Pictures\Screenshots\Screenshot 2026-07-01 230413.png")
## Project Structure

```
Deepfake_Flask_Project

│
├── app.py
├── deepfake_detector.keras
├── requirements.txt
│
├── templates
│     └── index.html
│
├── static
│     └── style.css
│
└── README.md
```

---

## Installation

```bash
git clone <repository-link>

cd Deepfake_Flask_Project

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## Conclusion

This project demonstrates the use of Deep Learning and Flask deployment for detecting manipulated images. The CNN model learns visual features from Real and Fake images and provides automated deepfake detection through a web application.

---

## Author

**HASNA FATHIMA H**

**Project: Deepfake Image Detection Using CNN and Flask**