import os
os.system('cls')

# ماشین حسابی برای چهار عملگر اصلی تعریف کنید که با دریافت کارکتر @ خاتمه یابد

while True :
    a = int(input('> a :'))
    b = int(input('> b :'))
    op = input('> op :')
    if op == '@' : break
    if op == '+' :
        print(a+b)
    elif op == '-' :
        print(a-b)
    elif op == '*' :
        print(a*b)
    else:
        try :
            print(int(a/b))
        except :
            while b==0:
                b = int(input('> b :'))
            print(int(a/b))
print('end')