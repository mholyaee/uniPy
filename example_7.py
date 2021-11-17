import os
os.system('cls')

#برنامه ای بنویسید که دو عدد از کاربر دریافت کرده و بازه اعداد بین این دو عدد را چاپ کند

#       الگوریتم اول        #
a = int(input('a :'))
b = int(input('b :'))
for i in range(a, b+1):
    print(i)

#       الگوریتم دوم        #
a = int(input('a :'))
b = int(input('b :'))
temp = ''

for i in range(a, b+1):
    temp = temp + str(i) + ' '

print(temp)
