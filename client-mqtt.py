import paho.mqtt.client as mqtt
import os

def on_message(client, userdata, message):
    message = message.payload.decode('utf-8')

    sub = os.popen(f'python3 req-anki.py {message}')
    sub.close()

    sub = os.popen(f'python3 main.py anki.tsv')
    sub.close()


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
