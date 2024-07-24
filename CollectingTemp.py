import serial 
import time 
import csv


# Initialize serial connection
ser = serial.Serial('COM9', 9600, timeout=1)  

# Define CSV name
csv_file = "DHT22_data.csv"

# Setting the CSV file
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature", "Humidity"])

    print("Starting data collection")
    try:
        while True:
            # Read data from sensor through the serial 
            line = ser.readline().decode('utf-8').strip()
            #if data is received
            if line:
                # Get time
                timestamp = time.strftime('%Y%m%d%H%M%S')
                data = line.split(',')

                # Write the data into the CSV file
                writer.writerow([timestamp] + data)

                # Print with the timestamp
                print(f"{timestamp}: {data}")

    except KeyboardInterrupt:
        # Stop data collection on keyboard interrupt
        print("Data collection stopped.")

