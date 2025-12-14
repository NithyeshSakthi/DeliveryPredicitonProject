from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained pipeline
model = joblib.load("ml_model.pkl")

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

        # Predict
        prediction = model.predict(input_data)[0]

        result = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0]
            delay_prob = proba[1]  # probability of class 1 (Delayed)

            # Debug prints (check terminal logs)
            print("DEBUG: prediction =", prediction)
            print("DEBUG: probabilities =", proba)

            # Decision logic
            if prediction == 1:
                if delay_prob >= 0.6:
                    result = "Delayed"
                else:
                    result = "On Time"
            elif prediction == -1:
                result = "Pending / Unknown"
            else:
                result = "On Time"
        else:
            if prediction == 1:
                result = "Delayed"
            elif prediction == -1:
                result = "Pending / Unknown"
            else:
                result = "On Time"

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template("index.html", prediction=result)

if __name__ == '__main__':
    app.run(debug=True)