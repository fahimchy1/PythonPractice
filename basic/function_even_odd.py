def pl():
    print('---------------------------------------------------')
def print_even_numbers(start,stop):
    for i in range(start,stop):
        if i%2==0:
            print('Even:- ', i)
        else:
            print('Odd:- ', i)
a=int(input())
b=int(input())
print_even_numbers(a,b)
pl()
a=int(input())
b=int(input())
b=b+1
print_even_numbers(a,b)

