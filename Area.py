#19 oct 2024
###### TRiangle, Rectangle , Trapezoid, Ellipse ,  Square, Parallelogram, Circle, Sector

base=float(input("Enter your base: "))
hight=float(input("Enter your hight: "))

########## Triangle
area=0.5*base*hight
print("Triangle Area= ",area,)

######## Rectangle
area=base*hight
print("Rectangle Area= ",area,)

#### Ellipse
area=3.1416*base*hight
print("Ellipse Area= ",area,)

##########Squard
area=base*base
print("Squard Area= ",area,)

##### Circle
area=3.1416*base*base
print("Circle Area= ",area,)

###### Parallelogram
area=base*hight
print("Parallelogram Area= ",area,)

####### Sector
area=0.5*base*base*hight
print("Sector Area= ",area,)

##### Trapezoid
print("=====FOR Trapezoid======= ")
a=float(input("Enter your a: "))
b=float(input("Enter your b: "))
h=float(input("Enter your h: "))
area=0.5*(a+b)*h
print("Trapezoid Area= ",area,)