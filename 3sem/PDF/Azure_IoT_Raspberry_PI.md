# Azure - IoT - Raspberry PI


## Setup an IoT Hub in Microsoft Azure



## Setup Raspberry PI to use Azure IoT for Python
On the Raspberry Pi and I used the official Microsoft IoT quick start for Python. 

This was used to create a sample IoT device and add the connection string to my IoT Hub. 

That project is referenced below.

https://github.com/Azure-Samples/azure-iot-samples-python/archive/master.zip

Run this command on the Raspberry Pi

    pip3 install azure-iot-device

Here I am customizing the example code to formulate sensor data received from the Sense Hat. 

I am using Red and Blue colors for Temp and Humidity.




import random  
from sense_hat import SenseHat
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Sense Hat
sense = SenseHat()

CONNECTION_STRING = "HostName=raspberrysense.azure-devices.net;DeviceId=xxxxxx;SharedAccessKey=xxxxxxxxxxxxxxxxxxx" 
# CONNECTION_STRING = "HostName=xxxxxxxx;DeviceId=xxxxxx;SharedAccessKey=xxxxxxxxxxxxxxxxxxx" 
MSG_SND = '{{"temperature": {temperature}}}' 

while True:
    temperature = str(round(sense.get_temperature(),2))
    def iothub_client_init():  
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
        return client  
    def iothub_client_telemetry_sample_run():  
        try:  
            client = iothub_client_init()  
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
            while True:  
                msg_txt_formatted = MSG_SND.format(temperature=temperature)  
                message = Message(msg_txt_formatted)  
                print( "Sending message: {}".format(message) )  
                client.send_message(message)  
                print ( "Message successfully sent" )  
                time.sleep(3)  
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )  
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()

