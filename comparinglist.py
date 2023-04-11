list1 = [10, 20, 30, 40, 50, 60] #created list 1
list2 = [10, 20, 30, 50, 40, 60,60] #created list 2

if len(list1)==len(list2):
    list1.sort() #sorting the list
    list2.sort() #soritng the list
    for i in range(0,len(list1)): #starting the of iteration of size of list
        if list1[i]!=list2[i]:
          
            print("list are not same") 
            break #using break to stop if both are not same
        if len(list1)-1==i : #since we have started with 0 , hence we to subtract 1
            print("both are same")
else:
    print("list are same")
