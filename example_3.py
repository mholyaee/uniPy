import os
os.system('cls')

# برنامه ای بنویسید که سه عدد از کاربر دریافت کند و بزرگترین عدد را نمایش دهد.

a, b, c = input('> ').split()
a = int(a)
b = int(b)
c = int(c)

max = a

if b > max :
    max = b
if c > max :
    max = c

print(max)