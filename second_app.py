from utils import apply_discount, greeting, discount

amount = apply_discount(100.50)
print(amount)

#Trying to change a member of the module here
discount = 0.50

#It does not work
print(apply_discount(100.50))

#We can change module members like this
import utils
utils.discount = 0.50
amount = apply_discount(100.50)
print(amount)