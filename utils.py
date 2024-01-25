discount = 0.10

def apply_discount(amount):
    return amount - (amount * discount)

def greeting(name):
    print("Hello", name)

def spam():
    print("This is just for fun")

print("You are loading the utils module. Thanks for using it")
spam()

#The module's code is executed in a separated environment
#If using a module in an interactive shell if make changes to module needs to restart shell to prevent reloading the module many times
#sys.modules.keys()
#returns a dictionary

