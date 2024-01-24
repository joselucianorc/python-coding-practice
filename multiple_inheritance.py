class Base(object):
    def spam(self):
        print("Base.spam")

class A(Base):
    def spam(self):
        print("A.spam")
        super().spam()

class B(A):
    def spam(self):
        print("B.spam")
        super().spam()

class C(A):
    def spam(self):
        print("C.spam")
        super().spam()

class Z(A):
    def spam(self):
        print("Z.spam")
        super().spam()

class D(B, A):
    def spam(self):
        print("D.spam")
        super().spam()

class X(B,C):
    pass

class E(D,C):
    pass

base = Base()
base.spam()

print("")

a = A()
a.spam()

print("")

b = B()
b.spam()

print("")

c = C()
c.spam()

z = Z()
z.spam()

B.__mro__

X.mro()
E.mro()

class QuotedMixin(object):
    def row(self, row_values):
        quoted_values = ['"{}"'.format(value) for value in row_values]
        super().row(quoted_values)


# from purchased_item_class import read_shopping_data
# from abstract_classes import CSVTAbleFormatter, HTMLTableFormatter, print_table

# class CustomFormatter(QuoteMixin, CSVTableFormatter):
#     pass

# CustormFormatter.mro()

# formatter = CustomFormatter()
# data = read_shopping_data("data/ecommerce_transactions.csv")
# print_table(data, ["name", "purchased_quantity", "price"], formatter)
    