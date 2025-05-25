from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

app = Flask(__name__)

     # Fake data to train the model
data = {
         'current_weight': [80, 90, 75, 85, 70, 95, 82, 78, 88, 92],
         'exercise_hours': [5, 3, 6, 4, 7, 2, 5, 6, 3, 4],
         'calorie_intake': [2000, 2200, 1800, 2100, 1900, 2300, 2000, 1950, 2150, 2250],
         'weeks_to_goal': [12, 15, 10, 13, 8, 18, 11, 9, 14, 16]
     }
df = pd.DataFrame(data)

     # Train a simple model
X = df[['current_weight', 'exercise_hours', 'calorie_intake']]
y = df['weeks_to_goal']
model = LinearRegression()
model.fit(X, y)

     # Save the model
with open('model.pkl', 'wb') as f:
         pickle.dump(model, f)

     # Load the model
with open('model.pkl', 'rb') as f:
         model = pickle.load(f)

@app.route('/')
def home():
         return open('index.html').read()

@app.route('/<path:filename>')
def serve_static(filename):
         return send_from_directory('.', filename)

@app.route('/predict', methods=['POST'])
def predict():
         data = request.get_json()
         current_weight = float(data['current_weight'])
         target_weight = float(data['target_weight'])
         exercise_hours = float(data['exercise_hours'])
         calorie_intake = float(data['calorie_intake'])
         
         # Check if current weight is more than target weight
         if current_weight <= target_weight:
             return jsonify({'error': 'Current weight must be greater than target weight'})
         
         # Predict weeks to goal
         prediction = model.predict([[current_weight, exercise_hours, calorie_intake]])[0]
         if prediction < 0:
             prediction = 0  # No negative predictions
         return jsonify({'weeks': prediction})

if __name__ == '__main__':
         app.run(debug=True, host='0.0.0.0', port=5000)