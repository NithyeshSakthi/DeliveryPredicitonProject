# DELIVERY PREDICTION PROJECT

## Details:
A Flask-based machine learning application that predicts whether an order will be **On Time**, **Delayed**, or **Pending/Unknown** based on customer, order, and shipping details.

## live app URL
https://deliverypredicitonproject.onrender.com/
## GitHub link 
https://github.com/NithyeshSakthi/DeliveryPredicitonProject

## Features
- Web form built with Flask + HTML/CSS
- Predicts delivery status using a trained ML model (`ml_model.pkl`)
- Threshold adjustment (classify as delayed if probability ≥ 0.6)
- Balanced dataset with oversampling for fair predictions
- Clean UI with dropdowns for payment type and shipping mode

## Project Structure
Delivery_Prediciton_Project/
├── app.py                     # Flask backend
├── ml_model.py                # Training script
├── ml_model.pkl               # Saved ML model
├── delay.csv                  # Dataset
├── incom2024_delay_variable_description.csv  # Variable descriptions
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── runtime.txt
├── Procfile
├── static/
│   ├── plots/				   # Saved visual graphs	
│   ├── logistics-customer-portal-2.jpg #Background template logo
│   └── styles.css             # CSS styles
├── docs					   # Sample screen shot refernces
└── templates/
    └── index.html             # HTML frontend
	

#How to run the flask app
python app.py

## How to Run Locally
```bash
python app.py

#local meachine
 Running on http://127.0.0.1:5000

#Deployment
This project is deployed using Render ![render success.png](docs/render%20success.png)

### predicition: ontime
sales_per_customer: 126.72665
latitude: 30.39185
Longitude: -111.95882
order_item_discount:20
order_item_discount_rate: 0.13
order_item_profit_ratio: 0.26
order_item_quantity: 3
order_profit_per_order: 35.82906
shipping_delay_days:39
payment_type: debit
shipping_mode: standard

### prediction: Delay
sales_per_customer: 89.96643
latitude: 18.2941
longitude: -66.037056
order_item_discount: 6.6
order_item_discount_rate: 0.06
order_item_profit_ratio: 0.09
order_item_quantity: 2
order_profit_per_order: 6.9655495
shipping_delay_days: (shipping_date - order_date) = 76 days
payment_type: DEBIT
shipping_mode: Second Class

### prediction: unknown
sales_per_customer: 250.0        
latitude: 52.52                 
longitude: 13.40                 
order_item_discount: 15.0          
order_item_discount_rate: 0.10     
order_item_profit_ratio: 0.05      
order_item_quantity: 3             
order_profit_per_order: 12.5      
shipping_delay_days: 2            
payment_type: Credit Card     
shipping_mode: Second Class

#Sample Output
![ontimeScreenshot 2025-12-16 012611.png](docs/ontimeScreenshot%202025-12-16%20012611.png)
![delayedScreenshot 2025-12-16 012349.png](docs/delayedScreenshot%202025-12-16%20012349.png)
![unkownScreenshot 2025-12-16 012158.png](docs/unkownScreenshot%202025-12-16%20012158.png)

#Author 
**Nithyesh Sakthi**
**Subham Sahu**