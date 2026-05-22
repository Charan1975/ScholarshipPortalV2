import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv('dataset.csv')

# Features
X = data[['cgpa', 'income', 'attendance', 'backlogs']]

# Target
y = data['eligible']

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, 'scholarship_model.pkl')

print("Model Trained Successfully!")