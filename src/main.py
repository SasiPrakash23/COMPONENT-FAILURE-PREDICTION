import pandas as pd
from model import train_model, predict_rul
from recommendations import generate_recommendations

# Load datasets
sensor_data = pd.read_csv('data/sensor_readings.csv')
threshold_data = pd.read_csv('data/threshold_values.csv')

# Merge datasets on Component_ID
merged_data = pd.merge(sensor_data, threshold_data, on='Component_ID')

# Feature engineering
merged_data['Temperature_Exceed'] = merged_data['Temperature'] > merged_data['Temperature_Threshold']
merged_data['Pressure_Exceed'] = merged_data['Pressure'] > merged_data['Pressure_Threshold']
merged_data['Vibration_Exceed'] = merged_data['Vibration'] > merged_data['Vibration_Threshold']
merged_data['Hour'] = pd.to_datetime(merged_data['Timestamp']).dt.hour
merged_data['Day'] = pd.to_datetime(merged_data['Timestamp']).dt.day

# Rolling averages for sensor readings
merged_data['Rolling_Temperature'] = merged_data.groupby('Component_ID')['Temperature'].rolling(window=2).mean().reset_index(0, drop=True)
merged_data['Rolling_Pressure'] = merged_data.groupby('Component_ID')['Pressure'].rolling(window=2).mean().reset_index(0, drop=True)
merged_data['Rolling_Vibration'] = merged_data.groupby('Component_ID')['Vibration'].rolling(window=2).mean().reset_index(0, drop=True)

# Fill NaN values
merged_data.fillna(method='bfill', inplace=True)

# Create a new RUL column
merged_data['RUL'] = 200 - merged_data['Operational_Hours']

# Train the model and make predictions
X, y = merged_data.drop(['RUL', 'Timestamp'], axis=1), merged_data['RUL']
rf_model = train_model(X, y)

# Generate recommendations
recommendations = generate_recommendations(merged_data, rf_model)
for rec in recommendations:
    print(rec)

# Example of predicting RUL for new sensor readings
new_input = pd.DataFrame({
    'Temperature': [78],
    'Pressure': [1.6],
    'Vibration': [0.05],
    'Rolling_Temperature': [77],
    'Rolling_Pressure': [1.5],
    'Rolling_Vibration': [0.045],
    'Temperature_Exceed': [0],
    'Pressure_Exceed': [0],
    'Vibration_Exceed': [1],
    'Operational_Hours': [400],
    'Hour': [12],
    'Day': [16]
})

predicted_rul = predict_rul(rf_model, new_input)
print(f'Predicted Remaining Useful Lifetime: {predicted_rul} days')
