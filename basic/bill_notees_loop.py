
bill=int(input('please input your bill:- '))
li=[1000,500,200,100,50,20,10,5,2,1]

for i in li:
    print(i,"note needed ",bill//i)
    bill=bill%i