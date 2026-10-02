# House Price Prediction

A Machine Learning web application that predicts house prices based on important house features.

## Project Overview

This project uses a Machine Learning regression model to predict the selling price of a house.

The model is trained using the Ames Housing dataset and is deployed as a web application using Flask.

Users can enter house details through a simple web form and get a predicted house price.

## Features

- House price prediction using Machine Learning
- Random Forest Regression model
- Simple Flask web application
- HTML and CSS frontend
- Predicted price displayed in Indian Rupees (₹)
- Easy-to-use input form

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS
- Jupyter Notebook

## Machine Learning Model

The project uses a Random Forest Regressor.

The model is trained using the following features:

- Overall Quality
- Living Area
- Garage Cars
- Total Basement Area
- First Floor Area
- Full Bathrooms
- Year Built
- Total Rooms Above Ground

## Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   └── train.csv
│
├── model/
│   └── house_price_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore