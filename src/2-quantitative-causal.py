import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('./data/filtered/Yogyakarta.csv')

X_humidity = df[['humidity']].values  # Feature: Humidity
y_temperature = df['tempC'].values  # Target: Temperature (Celsius)

X_train_hum, X_test_hum, y_train_temp, y_test_temp = train_test_split(X_humidity, y_temperature, test_size=0.2, random_state=42)

model_humidity = LinearRegression()
model_humidity.fit(X_train_hum, y_train_temp)

y_pred_temp = model_humidity.predict(X_test_hum)

mse_humidity = mean_squared_error(y_test_temp, y_pred_temp)
r2_humidity = r2_score(y_test_temp, y_pred_temp)

print(f'Mean Squared Error: {mse_humidity}')
print(f'R-squared Score: {r2_humidity}')

def predict_temperature(humidity_value):
    return model_humidity.predict([[humidity_value]])[0]

humidity_range = np.linspace(X_humidity.min(), X_humidity.max(), 100).reshape(-1, 1)
predicted_temperatures = model_humidity.predict(humidity_range)

plt.scatter(X_humidity, y_temperature, color='blue', label='Actual Data', alpha=0.5)
plt.plot(humidity_range, predicted_temperatures, color='red', label='Regression Line')

# Input and validation
valid_input = False
try:
    humidity_example = int(input("Input humidity value (0-100): "))
    if humidity_example < 0 or humidity_example > 100:
        raise ValueError("Invalid humidity value")
    valid_input = True
except ValueError as e:
    print(str(e))

if valid_input:
    predicted_temperature_example = predict_temperature(humidity_example)
    print(f'Predicted temperature at {humidity_example}% humidity: {predicted_temperature_example}°C')

    a = model_humidity.coef_
    b = model_humidity.intercept_

    print(f"Rumus Regresi Linear: y = {a[0]}x + {b}")

    plt.scatter(humidity_example, predicted_temperature_example, color='green', label=f'Predicted Temp at {humidity_example}% Humidity', marker='x', s=100)

    plt.xlabel('Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature vs. Humidity with Linear Regression')
    plt.legend()
    plt.show()

