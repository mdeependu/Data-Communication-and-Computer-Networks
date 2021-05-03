#7 BIT HAMMING CODE

lst=[0,0,0,0,0,0,0]
parityBits=[]

dataBit=input("please enter the data bit(4 bits)")

"""---------------------------Sender part-----------------------------"""

for i in range(0,7):
    temp=2**i
    if(temp<len(lst)):
        parityBits.append(temp-1)
#print(parityBits)
    

for i in range(len(lst)):
    if i in parityBits:
        lst[len(lst)-i-1]='P'
    else:
        lst[len(lst)-i-1]='D'
#print(lst)

increment=0
for j,i in zip(range(7),lst):
    if i=='D':
        lst[j]=dataBit[increment]
        increment=increment+1

j=len(lst)
binParity=[]
Dict={}
for i in lst:
    
    if i=='P':
        #print("P positn :",j)
        binParity.append(j)
    else:
        #print("D positn :",j)
        Dict.update({j:('00'+str(bin(j))[2::])})
    j=j-1

#print(Dict,binParity)


finParitysel=[]
for i in range(-1,-4,-1):
    Paritysel=[]
    for key in Dict:
        #print()
        #print(key,'->',Dict[key])
        temp=Dict[key][i]
        if temp=='1' :
            Paritysel.append(key)
        
    finParitysel.append(Paritysel)
    #print("------")
    
        
finParitysel.reverse()
#print(finParitysel)
#print(type(finParitysel[0][0]))
#print("input",lst)

result=[]

for i in finParitysel:
    for j in i:
        temp=len(lst)-j
        if lst[temp] in ['0','1']:
            result.append(int(lst[temp]))
        #print("result is:",result)
    if result.count(1)%2==0:
        #print("under if")
        for i,j in zip(range(len(lst)),lst):
            if j=='P':
                lst[i]=0
                break
                       
    else:
        for i,j in zip(range(len(lst)),lst):
            if j=='P':
                lst[i]=1
                break
    
    
    result=[]


sender=[]
for i in lst:
    sender.append(int(i))

print("message send in binary form using hamming code method",sender)
        
'''----------------------------------Destination end------------------------------'''

recieved=[1,1,1,0,1,0,1]

    




        
