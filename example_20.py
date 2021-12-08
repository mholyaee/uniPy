import os
os.system('cls')

# برنامه ای بنویسید که یک عدد از کاربر دریافت و بصورت زیر نمایش دهد :
# Result is : 3   9   8   7   5

x = input('> ')
print('Result is :\t', end='')
for i in x :
    print(i, end='\t')