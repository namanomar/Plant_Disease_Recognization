# 🌿 Plant Disease Recognition App

## 🌟 Overview

This project is a **Plant Disease Recognition Application** built using **Streamlit** for the frontend and **TensorFlow** for the backend. The app utilizes a **Convolutional Neural Network (CNN)** model to detect and classify diseases in plant leaves. It provides an intuitive interface to upload images of plant leaves and returns predictions on the disease affecting the plant and we get accuracy of  0.9813. 

## 🛠 Features

- 🖼️ **Image Upload**: Upload images of plant leaves through a simple interface.
- ⚡ **Real-time Disease Prediction**: Get instant predictions on the disease affecting the plant.
- 🤖 **CNN Model**: The app uses a trained Convolutional Neural Network (CNN) for accurate disease recognition.
- 🖥️ **Streamlit Interface**: A lightweight, responsive, and user-friendly interface for easy navigation.
- 🔗 **TensorFlow Integration**: Leverages TensorFlow to run the deep learning model efficiently.

## 🚀 Technologies Used

- **Frontend**: Streamlit
- **Backend**: TensorFlow, Python
- **Machine Learning Model**: Convolutional Neural Network (CNN)
- **Libraries**: 
  - `streamlit`
  - `tensorflow`
  - `opencv`
  - `numpy`
  - `matplotlib`
## 📋 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plant-disease-recognition.git
   ```
2. Navigate to the project directory:
```
cd plant-disease-recognition

```
3. Get the dataset from kaggle
```
Download the required api key from user section and place it on 
os.environ['KAGGLE_USERNAME'] = 'YOUR_USER_NAME'
os.environ['KAGGLE_KEY'] = 'YOUR_API_KEY'
After this run dataset.py to retrive the dataset
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```

5. Download the pretrained checkpoint from here : [Pretrained Checkpoint](https://drive.google.com/file/d/19g1cVj90SoBH5NCCVAY3_BoX55hNLRlT/view?usp=sharing) and place it on pretrained_datasets folder


6. Run the application:

```
streamlit run app.py
```
