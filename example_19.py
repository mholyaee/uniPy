import os
os.system('cls')

# بررسی کنید با سه عدد وارد شده میتوان مثلث تشکیل داد یا خیر

a, b, c = input('> ').split()
a = int(a)
b = int(b)
c = int(c)

if a+b > c and a+c > b and b+c > a :
    print('yes')
else :
    print('no')