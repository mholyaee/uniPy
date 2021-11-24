import os
os.system('cls')

# برنامه بنویسید که تعداد عدد مشخص از کاربر دریافت کرده و تعداد اعدادی که از میانگین اعداد بزرگترن را نمایش دهد

sum=0
A = []
n = int(input('enter count of data : '))
for i in range(n):
    x = float(input('> '))
    sum += x
    A.append(x)

avg = sum / n
count = 0
for number in A :
    if number > avg :
        count+=1

print(count)
