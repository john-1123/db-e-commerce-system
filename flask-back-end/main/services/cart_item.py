from main.models._db import delete, save
from main.models.cart_item import CartItem
from main.schemas.cart_item import CartItemSchema


class CartItemService:
    def __init__(self):
        self.cart_schema = CartItemSchema()
        self.carts_schema = CartItemSchema(many=True)

    def get_all(self):
        cart = CartItem.query.all()
        return_list=[]
        for i in cart:
            return_dict=dict()
            return_dict["member_id"]=i.member_id
            return_dict["market_id"]=i.market_id
            return_dict["product_id"]=i.product_id
            return_dict["quntity"]=i.quntity
            return_list.append(return_dict)
        return return_list
    
    def get_all_by_member(self, member_id):
        item_list = CartItem.query.filter_by(member_id=member_id).all()
        return self.carts_schema.jsonify(item_list)
    
    def get(self, data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id']).all()
        return_list=[]
        for i in cart:
            return_dict=dict()
            return_dict["product_id"]=i.product_id
            return_dict["quntity"]=i.quntity
            return_list.append(return_dict)
        return return_list

    def create(self, data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id'],CartItem.product_id==data['product_id']).first()
        if not cart:
            new_cart = CartItem(
                member_id=data['member_id'],
                market_id=data['market_id'],
                product_id=data['product_id'],
                quntity=data['quntity']
            )
            # print("new cart = ",new_cart)
            save(new_cart)
            return{
                "member_id":data['member_id'],
                "market_id":data['market_id'],
                "product_id":data['product_id'],
                "quntity":data['quntity']
            }

    def update(self,data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id'],CartItem.product_id==data['product_id']).first()
        if cart:
            cart.quntity=data['quntity']
            save(cart)
            return{
                "member_id":data['member_id'],
                "market_id":data['market_id'],
                "product_id":data['product_id'],
                "quntity":data['quntity']
            }

    def delete_single(self, data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id'],CartItem.product_id==data['product_id']).first()
        if cart:
            delete(cart)
            return {
                "member_id":data["member_id"],                
                "market_id":data["market_id"],
                "product_id":data["product_id"]
            }
        
    def delete_all(self, data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id']).all()

        if len(cart)!=0:
            for i in cart:
                delete(i)
            return "All the record of User #"+str(data['member_id'])+" in market #"+str(data['market_id'])+" has been deleted"


    def delete_all_by_member(self, data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id']).all()

        delete_cart_list=[]

        if len(cart)!=0:
            for i in cart:
                return_dict=dict()
                return_dict['member_id']=i.member_id
                return_dict["market_id"]=i.market_id
                return_dict["product_id"]=i.product_id
                return_dict["quntity"]=i.quntity
                delete_cart_list.append(return_dict)
                delete(i)
            return delete_cart_list

    def delete_all_by_market(self, data):
        cart = CartItem.query.filter(CartItem.member_id==data['member_id'],CartItem.market_id==data['market_id']).all()
        
        delete_cart_list=[]

        if len(cart)!=0:
            for i in cart:
                return_dict=dict()
                return_dict['member_id']=i.member_id
                return_dict["market_id"]=i.market_id
                return_dict["product_id"]=i.product_id
                return_dict["quntity"]=i.quntity
                delete_cart_list.append(return_dict)
                delete(i)
            return delete_cart_list
