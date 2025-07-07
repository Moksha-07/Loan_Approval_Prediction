# 🏦 Loan Approval Prediction Analysis
This is a Flask-based machine learning web application that predicts whether a loan application will be approved or rejected based on user input. It uses a trained classification model and a user-friendly HTML interface for loan applicants.

## 📂 Project Structure
*Loan-Approval-Prediction/*
*│
├── app.py                         
├── Loan Prediction Dataset.csv    
├── models/
│   └── loan_prediction.pkl        
├── templates/
│   ├── index.html                 
│   └── result.html               *

## 🚀 How It Works
*User accesses the homepage and fills out the loan application form.*

*The form data is sent to the backend via POST request.*

*The loan_prediction.pkl model processes the input and returns a prediction.*

*The result (Approved / Rejected) is displayed on a result page.*

## 🧠 Model Features Used
*The model takes the following features as input:*

*Loan_ID*

*Gender (0 = Female, 1 = Male)*

*Married (0 = No, 1 = Yes)*

*Dependents (0, 1, 2, 3+)*

*Education (0 = Not Graduate, 1 = Graduate)*

*Self Employed (0 = No, 1 = Yes)*

*Applicant Income*

Coapplicant Income

Loan Amount

Loan Amount Term (in months)

Credit History (1.0 = Good, 0.0 = Bad)

Property Area (0 = Rural, 1 = Semiurban, 2 = Urban)

Total income (Applicant + Coapplicant) is also calculated internally before prediction.

