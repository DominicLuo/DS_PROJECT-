from flask import Blueprint, request, jsonify
from ..models.product_orders import ProductOrder
from .. import db

product_orders_blueprint = Blueprint('product_orders', __name__, url_prefix='/product_orders')


@product_orders_blueprint.route('/', methods=['GET'])
def get_product_orders():
    product_orders = ProductOrder.query.all()
    return jsonify([{'OrderID': po.OrderID, 'UserID': po.UserID, 'SupplierID': po.SupplierID, 'OrderDate': po.OrderDate,
                     'ArrivalDATE': po.ArrivalDATE, 'DeliveryStatus': po.DeliveryStatus} for po in product_orders])


@product_orders_blueprint.route('//int:order_id', methods=['GET'])
def get_product_order(order_id):
    product_order = ProductOrder.query.get_or_404(order_id)
    return jsonify(
        {'OrderID': product_order.OrderID, 'UserID': product_order.UserID, 'SupplierID': product_order.SupplierID,
         'OrderDate': product_order.OrderDate, 'ArrivalDATE': product_order.ArrivalDATE,
         'DeliveryStatus': product_order.DeliveryStatus})


@product_orders_blueprint.route('/', methods=['POST'])
def add_product_order():
    data = request.json
    new_product_order = ProductOrder(UserID=data['UserID'], SupplierID=data['SupplierID'],
                                     OrderDate=data.get('OrderDate'), ArrivalDATE=data.get('ArrivalDATE'),
                                     DeliveryStatus=data['DeliveryStatus'])
    db.session.add(new_product_order)
    db.session.commit()
    return jsonify({'message': 'Product Order added successfully'}), 201


@product_orders_blueprint.route('//int:order_id', methods=['PUT'])
def update_product_order(order_id):
    product_order = ProductOrder.query.get_or_404(order_id)
    data = request.json
    if 'UserID' in data: product_order.UserID = data['UserID']
    if 'SupplierID' in data: product_order.SupplierID = data['SupplierID']
    if 'OrderDate' in data: product_order.OrderDate = data.get('OrderDate')
    if 'ArrivalDATE' in data: product_order.ArrivalDATE = data.get('ArrivalDATE')
    if 'DeliveryStatus' in data: product_order.DeliveryStatus = data['DeliveryStatus']
    db.session.commit()
    return jsonify({'message': 'Product Order updated successfully'})


@product_orders_blueprint.route('//int:order_id', methods=['DELETE'])
def delete_product_order(order_id):
    product_order = ProductOrder.query.get_or_404(order_id)
    db.session.delete(product_order)
    db.session.commit()
    return jsonify({'message': 'Product Order deleted successfully'})


@product_orders_blueprint.route('/status/<status>', methods=['GET'])
def get_product_orders_by_status(status):
    orders_by_status = ProductOrder.query.filter_by(DeliveryStatus=status).all()
    return jsonify([{'OrderID': po.OrderID, 'UserID': po.UserID, 'SupplierID': po.SupplierID, 'OrderDate': po.OrderDate,
                     'ArrivalDATE': po.ArrivalDATE, 'DeliveryStatus': po.DeliveryStatus} for po in orders_by_status])


@product_orders_blueprint.route('/user/int:user_id', methods=['GET'])
def get_product_orders_by_user(user_id):
    orders_by_user = ProductOrder.query.filter_by(UserID=user_id).all()
    return jsonify([{'OrderID': po.OrderID, 'UserID': po.UserID, 'SupplierID': po.SupplierID, 'OrderDate': po.OrderDate,
                     'ArrivalDATE': po.ArrivalDATE, 'DeliveryStatus': po.DeliveryStatus} for po in orders_by_user])
