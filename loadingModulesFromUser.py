###################################################
# TAKING INTEGERS FROM THE USER MULTIPLE TIMES    #
# PYTHON PROGRAM                                  #
# CODED BY HARSH TIWARI                           #
####################################################
def binfile():
    import pickle
    file=open("data.dat","wb")
    while True:
        x=int(input("Enter the no. "))
        pickle.dump(x,file)
        ans=input("DO u want to enter more data , Y or N :")
        if ans.upper()=="N":
            break
    file.close()
    file=open("data.dat","rb")
    try :
        while True:
            y=pickle.load(file)
            print(y)
    except EOFError:
        pass
    file.close()
binfile()
