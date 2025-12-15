from flask import Flask, render_template, request
import pandas as pd
import joblib
from typing import Optional  # for Optional[float] type hints

app = Flask(__name__)

# Load the trained pipeline
model = joblib.load("ml_model.pkl")

# Decision thresholds
DELAY_THRESHOLD = 0.6      # >= 0.6 => Delayed
PENDING_LOWER = 0.4        # (0.4, 0.6) => Pending / Unknown band


def classify(prediction: int, delay_prob: Optional[float]) -> str:
    """
    Returns one of: "Delayed", "Pending / Unknown", "On Time"
    1. If model gives -1, preserve uncertainty.
    2. If we have delay probability, use thresholds to refine the class.
    3. If no probability is available, fall back to class label only.
    """
    # Preserve explicit unknown from model
    if prediction == -1:
        return "Pending / Unknown"

    # If probability is available, use it for three-way classification
    if delay_prob is not None:
        if delay_prob >= DELAY_THRESHOLD:
            return "Delayed"
        elif PENDING_LOWER < delay_prob < DELAY_THRESHOLD:
            return "Pending / Unknown"
        else:
            return "On Time"

    # Fallback when predict_proba is unavailable
    if prediction == 1:
        return "Delayed"
    else:
        return "On Time"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect inputs from the form
        sales_per_customer = float(request.form["sales_per_customer"])
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])
        order_item_discount = float(request.form["order_item_discount"])
        order_item_discount_rate = float(request.form["order_item_discount_rate"])
        order_item_profit_ratio = float(request.form["order_item_profit_ratio"])
        order_item_quantity = int(request.form["order_item_quantity"])
        order_profit_per_order = float(request.form["order_profit_per_order"])
        shipping_delay_days = int(request.form["shipping_delay_days"])
        payment_type = request.form["payment_type"]
        shipping_mode = request.form["shipping_mode"]

        # Build dataframe with same structure as training
        input_data = pd.DataFrame([{
            "sales_per_customer": sales_per_customer,
            "latitude": latitude,
            "longitude": longitude,
            "order_item_discount": order_item_discount,
            "order_item_discount_rate": order_item_discount_rate,
            "order_item_profit_ratio": order_item_profit_ratio,
            "order_item_quantity": order_item_quantity,
            "order_profit_per_order": order_profit_per_order,
            "shipping_delay_days": shipping_delay_days,
            "payment_type": payment_type,
            "shipping_mode": shipping_mode
        }])

        # Predict class
        prediction = model.predict(input_data)[0]

        # Predict probability if available
        delay_prob: Optional[float] = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0]
            delay_prob = float(proba[1])  # probability of class 1 (Delayed)
            print(f"DEBUG: prediction={prediction} delay_prob={delay_prob} proba={proba}")

        # Apply corrected three-way classification (works with or without probability)
        result = classify(prediction, delay_prob)

    except Exception as e:
        result = f"Error: {str(e)}"

    # Frontend result
    return render_template("index.html", prediction=result)


if __name__ == '__main__':
    app.run(debug=True)