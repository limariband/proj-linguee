import paho.mqtt.client as mqtt
import os

def on_message(client, userdata, message):
    msg = message.payload.decode('utf-8')

    sub = os.popen(f'python3 main.py {msg} english language')
    sub.close()

    sub = os.popen(f'python3 req-anki.py dbase.tsv')
    sub.close()


if __name__ == '__main__':

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
