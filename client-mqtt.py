import paho.mqtt.client as mqtt
from main import main

def on_message(client, userdata, message):
    main({message.payload.decode('utf-8')})

topic = 'reqs'
broker = 'test.mosquitto.org'

client = mqtt.Client('br.tr.01')

client.on_message = on_message
client.connect(broker)
client.subscribe(topic)

try:
    client.loop_forever()
except KeyboardInterrupt as err:
    exit('Keyboard Interrupt')
