#########################
#Python File Handling   #
#Basic Operations       #
#CODED BY HARSH TIWARI  #
#########################
textFile= open("test.txt","w")
textFile.write("This is the first class in practically app")
textFile.close()
textFile=open("test.txt","a")
textFile.write("This is the Scond class in practically app")
textFile.close()
textFile=open("test.txt","r")
a=textFile.read()
textFile.close()
print(a)






              
