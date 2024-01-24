class PurchasedItem(object):

    def __init__(self, id, account, purchased_quantity,
                 item_name, item_quantity, item_unit,
                 item_price, category):

        self.id = id
        self.account = account
        self.purchased_quantity = purchased_quantity
        self.name = item_name
        self.quantity = item_quantity
        self.unit = item_unit
        self.price = item_price
        self.category = category


    def subtotal(self):
        return self.purchased_quantity * self.price
    
    def change_price(self, price):
        self.price = price

