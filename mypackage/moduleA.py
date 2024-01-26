import sys

from .subpackage1.moduleX import spam_x, default_x
from .subpackage1.moduleY import spam_y
from .subpackage2.moduleZ import spam_z

def spam_a():
    spam_x()
    print("spam from A module")
    print(default_x)

def another_spam():
    spam_y()
    print("another spam from A module")

if __name__ == "__main__":
    print(default_x)
    spam_x()

    print(sys.path)
    
    print(__name__)

    spam_a()
    another_spam()
    spam_z()
    

print(__name__)

# Use the -m argument to execute as a module
#python3 -m moduleA
