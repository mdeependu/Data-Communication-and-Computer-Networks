def division(dataBits,divisor,passBits,start,end):
    global temp
    temp=[]
    
    if(passBits[0]^divisor[0]==0):
        temp=temp+[passBits[1]^divisor[1]]
        temp=temp+[passBits[2]^divisor[2]]
        temp=temp+[passBits[3]^divisor[3]]

        if(end>len(dataBits)-1):
            
            print("Remainder: ",temp)
            for i in temp:
                if i==1:
                    print("error found")
            
            return 0
            
        
        else:
            temp=temp+[dataBits[end]]
            
          
    else:
        if(end>len(dataBits)-1):
            temp=passBits[1:5]
            print("Remainder : ",temp)
            for i in temp:
                if i==1:
                    print("error found")
            
            return 0

        temp=temp+[passBits[1]^0]
        temp=temp+[passBits[2]^0]
        temp=temp+[passBits[3]^0]

        temp=temp+[dataBits[end]]
       
    passBits=[]
    passBits=temp
    start=start+1
    end=end+1

    division(dataBits,divisor,passBits,start,end)

data = int(input("Enter Data Bits: "))
divisor = (input("Enter 4 bit: "))

lenDivisor = len(divisor)
dividend = str(data)+str(0)*(lenDivisor-1)
lenDividend = len(dividend)
start=0

dataBits=[]
divisorBits=[]
passBits=[]

for i in dividend:
    dataBits.append(int(i))

for j in divisor:
    divisorBits.append(int(j))

end=len(divisorBits)
for i in range(len(divisorBits)):
    passBits.append(dataBits[i])

print("dataBits are : ",dataBits)
print("Divisor bits are",divisorBits)


division(dataBits,divisorBits,passBits,start,end)

dataBits.pop(-1)
dataBits.pop(-2)
dataBits.pop(-3)

dataBits.append(temp[0])
dataBits.append(temp[1])
dataBits.append(temp[2])
print("\n\nSender:\ndataBits after encoding is :  ")

print(dataBits)

print("\n\nReciever:")
division(dataBits,divisorBits,passBits,start,end)

for i,j in enumerate(temp):
    if(j==0 and i==len(temp)-1):
        print("Successfully recieved")
        