import csv


def read_shopping_data(filename):
    data = []
    with open(filename) as file:
        rows = csv.reader(file)
        header = next(file)
        for row in rows:        
            row[2] = int(row[2])
            row[6] = float(row[6])            

            record = {
                'id': row[0],
                'account': row[1],
                'purchased_quantity': row[2],
                'item_name': row[3],
                'item_quantity': row[4],
                'item_unit': row[5],
                'item_price': row[6],
                'category': row[7]
            }

            data.append(record)
    
    return data

