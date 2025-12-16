from flask import Flask, render_template, request
import pandas as pd
import joblib
from typing import Optional  # for Optional[float] type hints

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is the about page."

# Load the trained pipeline
model = joblib.load("ml_model.pkl")

# Decision thresholds
DELAY_THRESHOLD = 0.6      # >= 0.6 => Delayed
PENDING_LOWER = 0.4        # (0.4, 0.6) => Pending / Unknown band

def classify(prediction: int, delay_prob: Optional[float]) -> str:
    """Returns one of: "Delayed", "Pending / Unknown", "On Time"."""
    if prediction == -1:
        return "Pending / Unknown"
    if delay_prob is not None:
        if delay_prob >= DELAY_THRESHOLD:
            return "Delayed"
        elif PENDING_LOWER < delay_prob < DELAY_THRESHOLD:
            return "Pending / Unknown"
        else:
            return "On Time"
    return "Delayed" if prediction == 1 else "On Time"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect inputs from the form
        input_data = pd.DataFrame([{
            "sales_per_customer": float(request.form["sales_per_customer"]),
            "latitude": float(request.form["latitude"]),
            "longitude": float(request.form["longitude"]),
            "order_item_discount": float(request.form["order_item_discount"]),
            "order_item_discount_rate": float(request.form["order_item_discount_rate"]),
            "order_item_profit_ratio": float(request.form["order_item_profit_ratio"]),
            "order_item_quantity": int(request.form["order_item_quantity"]),
            "order_profit_per_order": float(request.form["order_profit_per_order"]),
            "shipping_delay_days": int(request.form["shipping_delay_days"]),
            "payment_type": request.form["payment_type"],
            "shipping_mode": request.form["shipping_mode"]
        }])

        # Predict class
        prediction = model.predict(input_data)[0]

        # Predict probability if available
        delay_prob: Optional[float] = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0]
            delay_prob = float(proba[1])  # probability of class 1 (Delayed)
            print(f"DEBUG: prediction={prediction} delay_prob={delay_prob} proba={proba}")

        result = classify(prediction, delay_prob)

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)