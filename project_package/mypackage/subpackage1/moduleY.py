from .moduleX import spam_x, default_x

default_x = 2

def spam_y():
    spam_x()
    print("spam from Y module")

