import sys
from abc import ABC, abstractmethod

def print_table(objects, attributes_names):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Formatter must be a TableFormatter")
    
    for attr_name in attributes_names:
        print("{:>40s}".format(attr_name), end=" ")
    print("")

    for obj in objects:
        for attr_name in attributes_names:
            print("{:>40s}".format(str(getattr(obj, attr_name))), end=" ")
        print("")

def print_table(objects, attributes_names, formatter):
    formatter.headings(attributes_names)
    for obj in objects:
        row_values = [str(getattr(obj,attr_name)) for attr_name in attributes_names]
        formatter.row(row_values)


class TableFormatter(ABC):
    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, row_values):
        pass

# class TableFormatter(object):
#     def __init__(self, outfile=None):
#         if outfile == None:
#             outfile = sys.stdout
#         self.outfile = outfile

#     def headings(self, headers):
#         raise NotImplementedError
    
#     def row(self, row_values):
#         raise NotImplementedError

class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width=10):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile
        self.width = width

    def headings(self, headers):
        for header in headers:
            print("{:>{}s}".format(header, self.width), end=" ", file=self.outfile)
        print(file=self.outfile)

    def row(self, row_values):
        for value in row_values:
            print("{:>{}s}")



# class TextTableFormatter(object):
#     def __init__(self, outfile=None, width=10):
#         if outfile == None:
#             outfile = sys.stdout
#         self.outfile = outfile
#         self.width = width

#     def headings(self, headers):
#         for header in headers:
#             print("{:>{}s}".format(header, self.width), end=" ", file=self.outfile)
#         print(file=self.outfile)

#     def row(self, row_values):
#         for value in row_values:
#             print("{:>{}s}")

class CSVTableFormatter(object):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, row_values):
        print(",".join(row_values))

class HTMLTableFormatter(object):
    def headings(self, headers):
        print("<str", end=" ", file=self.outfile)
        for header in headers:
            print("<th>{}</th>".format(header), end="", file=self.outfile)
        print("</tr>", file=self.outfile)

    def row(self, row_values):
        print("<tr>", end="")
        for value in row_values:
            print("<td>{}</td>".format(value), end="", file=self.outfile)
        print("</tr>", file=self.outfile)


# item = PurchasedItem("123", "js.jetti@grwz.com", 10, "Milk", 
#                      1, "qt", 2.5, "dairy products")
# item


# csv_formatter = CSVTableFormatter()
# print_table(dataclasses, ["name", "purchased_quantity", "price"], csv_formatter)
# html_formatter = HTMLTableFormatter()
# print_table(data, ["name", "purchased_quantity", "price"], html_formatter)

# data = read_shopping_data("data/ecommerce_transactions.csv")
# from purchased_item_class import read_shopping_data
# data = read_shopping_data("data/ecommerce_transactions.csv")
# formatter = CSVTableFormatter()
# print_table(data, ["name", "purchased_quantity", "price"], formatter)
# formatter = HTMLTableFormatter()

class CustomTableFormatter(object):
    pass


from purchased_item_class import read_shopping_data
data = read_shopping_data("data/ecommerce_transactions.csv")
formatter = CustomTableFormatter()

