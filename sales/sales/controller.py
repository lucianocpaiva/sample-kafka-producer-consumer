from flask import request
from flask_restful import Resource
from .service import send_to_processing

class Sale(Resource):
 
    def __init__(self, **kwargs) -> None:

        self.producer = kwargs['producer']
        self.topic = kwargs['topic']

    def get(self):

        return [], 200

    def post(self):
        
        data = request.get_json()

        send_to_processing(self.producer, self.topic, data)

        return {'productId': data['productId'], 
                'message': 'Pedido realizado!'}, 201
