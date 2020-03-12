a=int(input('enter the number '))
while a!=0 :
    r=a%10
    if (r%2)!=0:
        print(r)
    a=int(a/10)
