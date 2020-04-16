##############################################
# code By Harsh Tiwari
# code for Fibonacci in python
##################################################
def Fibonacci(p):
    fab=[0,1]
    a=0
    b=1
    if p<=0:
        return print("Enter the valid number")
    if p==1:
        return fab.pop(0)
    for i in range(p-2):
        c=a+b
        a=b
        b=c
        fab.append(c)
    return fab
a=int(input("Enter number of output required"))
print(Fibonacci(a))
