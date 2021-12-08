import os
os.system('cls')

# برنامه ای بنویسید که بررسی کند عدد وارد شده ریشه سوم صحیح دارد یا خیر

n = int(input('> ')) # 125 - 126
for i in range(1, n) :
    if i*i*i > n :
        print("No")
        break
    if i*i*i == n :
        flag = True
        print("yes", str(i))
        break