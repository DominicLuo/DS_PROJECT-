from flask import Blueprint, request, jsonify
from ..models.food_order import FoodOrder
from .. import db

food_order_blueprint = Blueprint('food_order', __name__, url_prefix='/food_order')


@food_order_blueprint.route('/', methods=['GET'])
def get_food_orders():
    food_orders = FoodOrder.query.all()
    return jsonify([{'FDeliveryID': fo.FDeliveryID, 'DeliveryStatus': fo.DeliveryStatus, 'OrderTime': fo.OrderTime,
                     'SupplierID': fo.SupplierID, 'UserID': fo.UserID, 'CurrentLocation': fo.CurrentLocation,
                     'EstimateTime': fo.EstimateTime} for fo in food_orders])


@food_order_blueprint.route('/<int:fdelivery_id>', methods=['GET'])
def get_food_order(fdelivery_id):
    food_order = FoodOrder.query.get_or_404(fdelivery_id)
    return jsonify({'FDeliveryID': food_order.FDeliveryID, 'DeliveryStatus': food_order.DeliveryStatus,
                    'OrderTime': food_order.OrderTime, 'SupplierID': food_order.SupplierID, 'UserID': food_order.UserID,
                    'CurrentLocation': food_order.CurrentLocation, 'EstimateTime': food_order.EstimateTime})


@food_order_blueprint.route('/', methods=['POST'])
def add_food_order():
    data = request.json
    new_food_order = FoodOrder(DeliveryStatus=data['DeliveryStatus'], OrderTime=data['OrderTime'],
                               SupplierID=data['SupplierID'], UserID=data['UserID'],
                               CurrentLocation=data['CurrentLocation'], EstimateTime=data['EstimateTime'])
    db.session.add(new_food_order)
    db.session.commit()
    return jsonify({'message': 'Food Order added successfully'}), 201
