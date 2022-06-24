
from json import dumps

def send_to_processing(producer, topic, payload)-> None:
    
    data = str.encode(dumps(payload))

    producer.send(topic, data)
    producer.flush()