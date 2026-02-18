'''Create math_utils.py with functions for area of a circle, rectangle, and triangle. In main.py,
import and call each. Guard both files with if __name__=='__main__'.'''


import math_utils
print("Running")
if __name__ == '__main__':
    print("Area of circle : " ,math_utils.circle(9))
    print("Area of rectangle :" ,math_utils.rectangle(10,20))
    print("Area of triangle : " ,math_utils.triange(10,2))
