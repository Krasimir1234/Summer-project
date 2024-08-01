from flask_restx import Namespace,fields ,Resource
import requests
from src.car import Car

car_ns = Namespace('cars', description='Car related operations')

car_model=car_ns.model('Cars',{
    'id': fields.Integer(required = True),
    'model': fields.String(required = True)
})

@car_ns.route('/')
class CarOptions(Resource):
    @car_ns.marshal_with(car_model)
    @car_ns.doc(car_model)
    @car_ns.expect(car_model)
    def post(self):
        """Add a new car."""
        data = car_ns.payload
        new_car = Car(**data)
        new_car.add_to_database()
        return new_car, 201
