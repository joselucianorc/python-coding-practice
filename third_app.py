from utils import apply_discount as default_apply_discount

discount = 0.5

def apply_discount(amount):
    return amount - (amount * discount)

print(default_apply_discount(""))
