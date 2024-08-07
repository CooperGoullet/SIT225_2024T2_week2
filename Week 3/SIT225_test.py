import sys
import traceback
from arduino_iot_cloud import ArduinoCloudClient
from datetime import datetime
 
DEVICE_ID = "77129f4a-c609-424a-bd7c-78f19df35201"
SECRET_KEY = "G28ZCnoyY1zsteCjLqLdm5rWK"
 
csv_file = open('sensor_data_2.csv', mode='a', newline='')
csv_file.write("Timestamp, Temperature, Humidity\n")
 
def on_temperature_changed(client, value):
    print(f"New temperature: {value}")
    write_to_csv(value, None)
 
def on_humidity_changed(client, value):
    print(f"New humidity: {value}")
    write_to_csv(None, value)
 
def write_to_csv(temperature, humidity):
    timestamp = datetime.now().isoformat()
    if temperature is not None:
        csv_file.write(f"{timestamp}, {temperature},\n")
    elif humidity is not None:
        csv_file.write(f"{timestamp}, , {humidity}\n")
    csv_file.flush()

def main():
    print("main() function")
 
    client = ArduinoCloudClient(
        device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY
    )
 
    client.register("ptemp", value=None, on_write=on_temperature_changed)
    client.register("phum", value=None, on_write=on_humidity_changed)
 
    client.start()
 
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback)
        print(f"{exc_type.__name__}: {exc_value}")
    finally:
        csv_file.close()
 