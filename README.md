DELIVERY PREDICTION PROJECT

#Details:

A Flask-based machine learning application that predicts whether an order will be **On Time**, **Delayed**, or **Pending/Unknown** based on customer, order, and shipping details.

## Features
- Web form built with Flask + HTML/CSS
- Predicts delivery status using a trained ML model (`ml_model.pkl`)
- Threshold adjustment (classify as delayed if probability ≥ 0.3)
- Balanced dataset with oversampling for fair predictions
- Clean UI with dropdowns for payment type and shipping mode

Delivery_Prediciton_Project
-app.py		#Flask backend
-ml_model.py 		#Training Script
-ml_model.pkl 		#Saved ML model
-delay.csv 			#DataSet
-incom2024_delay_variable_description.csv 	#Variable descriptions
-requirements.txt			#Python Dependencies
-REDME.md			#Project Documentation
-static
	-plots 
	-logistics-customer-portal-2.jpg		#Templates
	-styles.css		#CSS Style
-templates
	-index.html #HTML Frontend
	

#How to run the flask app
python app.py


#browesr open 
 Running on http://127.0.0.1:5000

#Sample Input

sales_per_customer: 89.96643
latitude: 18.2941
longitude: -66.037056
order_item_discount: 6.6
order_item_discount_rate: 0.06
order_item_profit_ratio: 0.09
order_item_quantity: 2
order_profit_per_order: 6.9655495
shipping_delay_days: 76
payment_type: DEBIT
shipping_mode: SECOND


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




#Sample Output

• On Time (green)
• Delayed (red)

#Author 
Nithyesh Sakthi