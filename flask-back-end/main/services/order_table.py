from main.models._db import delete, save
from main.models.cart_item import CartItem
from main.models.order_table import Order_Table
from main.models.product import Product
from main.schemas.order_table import OrderSchema


class OrderService:
    def __init__(self):
        self.order_schema = OrderSchema()
        self.orders_schema = OrderSchema(many=True)

    def get(self, data):
        order = Order_Table.query.filter_by(order_id = data['order_id']).first()
      
        if order == None:
            return "not found"
        else: 
            return self.order_schema.jsonify(order)
    
    def get_all_order_by_market(self, market_id):
        order_list = Order_Table.query.filter_by(market_id = market_id).all()
        return self.orders_schema.jsonify(order_list)

    def get_all_order_by_member(self, user_id):
        order_list = Order_Table.query.filter_by(member_id = user_id).all()
        return self.orders_schema.jsonify(order_list)

    def create(self, data):
        items = CartItem.query.filter_by(member_id = data['member_id'], market_id = data['market_id']).all()

        cost = 0
        items_list = []
        quantity_list = []
        cash_list = []
        
        if len(items) == 0:
            return "Can't make order"
        
        for item in items:
            product_id = item.product_id
            demand = item.quantity
            
            this_product = Product.query.filter_by(product_id = product_id).first()
            price = this_product.price
            supply = this_product.stock
            item_name = this_product.product_name
            
            items_list.append(item_name)
            quantity_list.append(str(demand))
            cash_list.append(str(price*demand))
            
            if supply < demand:
                return "You Buy Too Much"
            else:
                cost += price * demand
            
        ### check 
        new_order = Order_Table(
            member_id = data['member_id'],
            market_id = data['market_id'],
            state = data['state'],
            shipping_address = data['shipping_address'],                
            consignee = data['consignee'],
            payment_method = data['payment_method'],
            mode_of_transport = data['mode_of_transport'],
            items = ",".join(items_list),
            quntities = ",".join(quantity_list),
            cashs = ",".join(cash_list),
            cost = cost
        )
        
        save(new_order)

        for item in items:
            print(item['quantity'])
            delete(item)

        return self.order_schema.jsonify(new_order)

    def delete(self, order_id):
        order = Order_Table.query.filter_by(order_id = order_id).first()
        if order:
            delete(order)
            return self.order_schema.jsonify(order)
