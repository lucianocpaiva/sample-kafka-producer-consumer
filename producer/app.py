import os
import json
from flask import Flask, request, jsonify
from kafka import KafkaProducer

TOPIC_NAME = "teste"
KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9092")

app = Flask(__name__)

app.logger.info('Initializing Kafka producer' + KAFKA_SERVER)

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
)

def send_to_processing(producer, json_payload: json)-> None:
    
    producer.send(TOPIC_NAME, json_payload)
    producer.flush()


@app.route('/')
def version():
    return jsonify({"version": "1.0.0"})

@app.route('/kafka/pushToConsumers', methods=['POST'])
def kafkaProducer():
		
    req = request.get_json()

    json_payload = str.encode(json.dumps(req))
	
    app.logger.info('Sending message to Kafka')

    send_to_processing(producer, json_payload)
    
    return jsonify({
        "message": "Seu pedido foi realizado com sucesso!"})


if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0')
