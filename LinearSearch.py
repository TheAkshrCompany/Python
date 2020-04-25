#################################################
##### CODED BY HARSH TIWARI
#################################################
def linearSearch(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i
    return -1
a=["sda","python","mac","pc"]
b="mac"
print("Element found at index "+str(linearSearch(a,b)))
