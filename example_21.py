import os
os.system('cls')

# برنامه ای برای محاسبه مقدار دنباله زیر با بنویسید :
# 1/1! + 1/2! + 1/3! + ... + 1/n!

def fac(n) -> int :
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input('> '))
sum = 0
for i in range(1, n+1) :
    sum = sum + (1/fac(i))

print(sum)