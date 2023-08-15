print("Message Encodor/Decodor")


def encoder():
    emsg=[]
    value=0
    message=input("Enter the message in binary -")
    for i in message:
        
        if i=='1':
           
            emsg.append(1)
            value=value+1
            if value==5:
                emsg.append('0')
                value=0
            
        elif i=='0':
            emsg.append(0)
    print("the encoded message is "+''.join([str(elem) for elem in emsg]))
def decoder():
    emsg=[]
    value=0
    i=0
    message=input("Enter the message in binary - ")
    while i < len(message):
      
       
        if message[i]=='1':
           
            emsg.append(1)
            value=value+1
            
            if value==5:
                i=i+1
                value=0
            
        elif message[i]=='0':
            emsg.append(0)
        i=i+1
            
    print("the encoded message is "+''.join([str(elem) for elem in emsg]))

while(True):
    print("\n1.Encode the message ")
    print("2.Decode the message ")
    choice=int(input("Enter your choice -"))
    if choice==1:
        encoder()
    elif choice==2:
        decoder()
    else:print("Enter the correct choice")
