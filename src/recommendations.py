def generate_recommendations(data, model):
    recommendations = []
    for index, row in data.iterrows():
        if row['RUL'] < 10:  # Custom threshold for recommendations
            recommendations.append(f"Component {row['Component_ID']} requires immediate attention! RUL is {row['RUL']} hours.")
        elif row['Temperature_Exceed'] or row['Pressure_Exceed'] or row['Vibration_Exceed']:
            recommendations.append(f"Check component {row['Component_ID']} as it exceeds operational thresholds.")
        else:
            recommendations.append(f"Component {row['Component_ID']} is operating within normal parameters.")

    return recommendations
