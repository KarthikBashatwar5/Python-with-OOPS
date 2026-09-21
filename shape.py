class shapes:
    name="shape name"
class circle(shapes):
    r=int(input("enter rvalue :"))
def area (self,r):
    area=3.14*r*r
    print("area of cicle")
class rectangle(shapes):
    L=int(input("enter length value:"))
    B=int(input("enter breadth value:"))
    def area (self,l,b):
        area_rec=l*b
        print("rectangle Area=")
class triangle (shapes):
    B=int(input("enter breadth value"))
    H=int(input("enter height value"))
    def area(self,b,h):
        area_tri=0.5*b*h
        print("area of triangle")
c=circle()
r=rectangle()
t=triangle()
c.area()
r.area()
t.area()

