import os
from flask import Flask
from flask_restful import Api
from kafka import KafkaProducer
from sales.controller import Sale

app = Flask(__name__)
api = Api(app)

TOPIC_NAME = os.getenv("TOPIC_SALES", "teste")
KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost:9092")

# Inicializando Kafka Producer
producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
)

kwargs = {
    'producer': producer, 'topic': TOPIC_NAME 
}

api.add_resource(Sale, '/sales', resource_class_kwargs=kwargs)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
