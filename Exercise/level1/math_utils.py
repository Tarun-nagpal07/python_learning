
def circle(r):
    return 3.14*r*r

def rectangle(l,b):
    return l*b

def triange(b,h):
    return 1/2 * h * b

print("outside __name__")


if __name__ == '__main__':
    print("Calculating ... : ")
    print("Area of circle : " ,circle(9))
    print("Area of rectangle :" ,rectangle(10,20))
    print("Area of triangle : " ,triange(10,2))