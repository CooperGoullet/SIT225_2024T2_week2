#include "DHT.h"

#define DHTPIN 3     
#define DHTTYPE DHT22  

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  

  Serial.print(t);
  Serial.print(",");
  Serial.println(h);
  delay(30000);
}

