from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model/house_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    overall_qual = float(request.form["OverallQual"])
    gr_liv_area = float(request.form["GrLivArea"])
    garage_cars = float(request.form["GarageCars"])
    total_bsmt_sf = float(request.form["TotalBsmtSF"])
    first_flr_sf = float(request.form["1stFlrSF"])
    full_bath = float(request.form["FullBath"])
    year_built = float(request.form["YearBuilt"])
    total_rooms = float(request.form["TotRmsAbvGrd"])

    # Arrange inputs in the same order used during training
    features = np.array([[
        overall_qual,
        gr_liv_area,
        garage_cars,
        total_bsmt_sf,
        first_flr_sf,
        full_bath,
        year_built,
        total_rooms
    ]])

    # Make prediction
    prediction = model.predict(features)[0]

    # Convert USD-style dataset price to INR
    USD_TO_INR = 85
    prediction_inr = prediction * USD_TO_INR

    return render_template(
        "index.html",
        prediction=f"₹{prediction_inr:,.0f}"
    )


if __name__ == "__main__":
    app.run(debug=True)