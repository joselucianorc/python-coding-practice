from purchased_item_class import PurchasedItem

def set_record(row):
    return {
        'id': row[0],
        'account': row[1],
        'purchased_quantity': row[2],
        'item_name': row[3],
        'item_quantity': row[4],
        'item_unit': row[5],
        'item_price': row[6],
        'category': row[7]
    }

item = PurchasedItem("123", "js.jetti@grwz.com", 10, "Milk", 
                     1, "qt", 2.5, "dairy products")
item

