n = int(input())
for i in range(n):
    x,y,z = [int(t) for t in input().split()]
    if x==y+z or y==x+z or z==y+x:
        print('Yes')
    else:
        print('No')


