#=====1=======

# n=int(input())
# li = [int(x) for x in input().split()]
#
# for i in range(0,len(li)):
#     if i%2==0:
#         print("Even", li[i])
#     else:
#         print("Odd", li[i])


#======2=======
li_1 = [1,2,3,4,5,6,7]
li_2 = [11,22,33,44]
li_3 = "i_am_dash"

for i in range(max(len(li_1),len(li_2),len(li_3))):
    if i<len(li_1):
        print(li_1[i], end=" ")
    else:
        print('*',end=' ')

    if i<len(li_2):
        print(li_2[i], end=" ")
    else:
        print('*',end=' ')

    if i<len(li_3):
        print(li_3[i])
    else:
        print('*')
