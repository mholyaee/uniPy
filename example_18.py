import os
os.system('cls')

# برنامه ای بنویسید که بررسی کند عدد وارد شده ریشه سوم صحیح دارد یا خیر
# با تابع

def rishe(n) -> int :
    for i in range(1, n):
        if i*i*i > n :
            return 0
        if i*i*i == n :
            return i

while True :
    num = int(input('> '))
    if not rishe(num) :
        print('Nope')
    else :
        print(f'yup : {rishe(num)}')