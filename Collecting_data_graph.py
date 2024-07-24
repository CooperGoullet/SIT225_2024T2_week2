import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("DHT22_data.csv")

# Convert timestamp
data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y%m%d%H%M%S')

# Plot
plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['Temperature'], label='Temperature')
plt.plot(data['Timestamp'], data['Humidity'], label='Humidity')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Temperature and Humidity over 30 mins')
plt.legend()
plt.show()
