# Customer Churn Prediction System

## Project Overview
This project is an end-to-end **Customer Churn Prediction system** built using Machine Learning.
The goal is to identify customers who are likely to stop using the service so that businesses can take proactive actions.

---

## Objective
- Predict customer churn using historical data  
- Understand customer behavior  
- Help businesses improve retention strategies  

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Git & GitHub  

---

## Project Structure
customer_churn_prediction/
│
├── data/
│ └── raw/
│ └── customers.csv
│
├── notebooks/
│ └── eda.ipynb
│
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── model_training.py
│ └── prediction.py
│
├── main.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## Workflow
1. Load customer data  
2. Perform exploratory data analysis (EDA)  
3. Feature engineering  
4. Train ML model (Random Forest)  
5. Generate churn predictions  

---

## Model Used
- **Random Forest Classifier**
- Evaluation Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score

---

## How to Run the Project

###  Install dependencies
```bash
pip install -r requirements.txt
