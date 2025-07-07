from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model = pickle.load(open(r"C:\Users\smoks\Loan_Prediction_Analysis\models\loan_prediction.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    loan_id = data['Loan_ID']

    # Prepare input data
    gender = int(data['Gender'])
    married = int(data['Married'])
    dependents = 3 if data['Dependents'] == '3+' else int(data['Dependents'])
    education = int(data['Education'])
    self_employed = int(data['Self_Employed'])
    applicant_income = float(data['ApplicantIncome'])
    coapplicant_income = float(data['CoapplicantIncome'])
    loan_amount = float(data['LoanAmount'])
    loan_amount_term = float(data['Loan_Amount_Term'])
    credit_history = float(data['Credit_History'])
    property_area = int(data['Property_Area'])

    # Add missing feature (likely TotalIncome)
    total_income = applicant_income + coapplicant_income

    input_data = np.array([[gender, married, dependents, education, self_employed,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_amount_term, credit_history, property_area, total_income]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = f"{loan_id} : Loan Approved"
    else:
        result = f"{loan_id} : Loan Rejected"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)