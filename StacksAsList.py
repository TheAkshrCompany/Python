###################################
# Implrenting list as stacks      #
# Pythom Code                     #
# Coded by Harsh Tiwari           #
###################################
l1=[] # Empty List
c="y" # Condition for while
while (c=="y"):
    print("1. Push \n 2.Pop \n 3.Display")
    choice=int(input("Enter your choice"))
    if choice==1:
        a=input("Enter any no.")
        l1.append(a)
    elif choice==2:
        if l1==[]:
            print("Your stack is empty")
        else :
            print("Deleted the element is ",l1.pop())
    elif choice==3:
        d=len(l1)
        for i in range (d-1,-1,-1):
            print("the list is ", l1[i])
    else :
        print("U have wntered the wrong choice ")
    c=input("Do u want to continue ")# if the user enter y then it restarts

