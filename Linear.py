def linearSearch(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i
    return -1
a=["sda","python","harsh","pc"]
b="harsh"
print("Element found at index "+str(linearSearch(a,b)))
