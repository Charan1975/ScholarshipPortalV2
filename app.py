from flask import Flask, render_template, request
import joblib
import sqlite3
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load('scholarship_model.pkl')


# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# PREDICTION ROUTE
@app.route('/predict', methods=['POST'])
def predict():

    # Get form data
    name = request.form['name']
    cgpa = float(request.form['cgpa'])
    income = float(request.form['income'])
    attendance = float(request.form['attendance'])
    backlogs = int(request.form['backlogs'])

    # Prepare data for prediction
    features = np.array([[cgpa, income, attendance, backlogs]])

    # Predict
    result = model.predict(features)

    # Prediction text
    if result[0] == 1:
        prediction = "Student is Eligible for Scholarships"
    else:
        prediction = "Student is NOT Eligible for Scholarships"

    # Connect SQLite database
    conn = sqlite3.connect('scholarship.db')

    cursor = conn.cursor()

    # Fetch matching scholarships
    cursor.execute("""
        SELECT scholarship_name, amount, official_link
        FROM Scholarships
        WHERE min_cgpa <= ?
        AND max_income >= ?
    """, (cgpa, income))

    scholarships = cursor.fetchall()

    conn.close()

    # Send data to result page
    return render_template(
        'result.html',
        prediction=prediction,
        scholarships=scholarships
    )


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)