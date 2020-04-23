import circle
import rectangle
a=int(input("Enter the Choice \n 1.Circumference of circle \n2.Area Of circle \n3.Perimeter of rect \n4. Area of rectangle \n5.Exit  - "))
if a==1:
    c=int(input("Enter the dimensions -"))
    print(circle.Circum(c))
if a==2:
    c=int(input("Enter the dimensions -"))
    print(circle.AreaCircle(c))
if a==3:
    c=int(input("Enter the dimensions -"))
    b=int(input("Enter the dimensions -"))
    print(rectangle.Perim(c,b))
if a==4:
    c=int(input("Enter the dimensions -"))
    f=int(input("Enter the dimensions -"))
    print(rectangle.Area(c,f))
if a==5:
    exit


