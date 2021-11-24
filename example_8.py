import os
os.system('cls')

# برنامه ای بنویسید که یک لیست از اعداد دریافت کرده و آنرا برعکس ترتیب وارد شده نمایش دهد

A = list()
n = int(input('> n : '))

for i in range(n):
    x = int(input('> '))
    A.append(x)

print(sorted(A, reverse=True))