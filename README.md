# Component Failure Prediction

## Overview
This project involves developing a smart AI solution to predict equipment/component failures based on historical and usage data to enhance equipment efficiencies for Caterpillar's global customers.

## Dataset
The project uses two datasets:
- **Sensor Readings**: Contains operational data from various components.
- **Threshold Values**: Contains predefined threshold values for components.

## Features
- Predict Remaining Useful Lifetime (RUL) of components.
- Generate actionable maintenance recommendations.
- Monitor sensor readings against threshold values.

## How to Run
1. Ensure you have Python and required packages installed.
2. Place the CSV files in the `data/` directory.
3. Run the main script:
   ```bash
   python src/main.py
