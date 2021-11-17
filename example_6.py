import os
os.system('cls')

# برنامه ای بنویسید که عددی از کاربر دریافت کند و مشخص کند اول است یا مرکب

#       الگوریتم اول        #
x = int(input('> '))
found = False

for i in range(2, x) :
    if x%i == 0 :
        found = True

if found == False:
    print('aval.')
else :
    print('Morakab.')

#       الگوریتم دوم        #
x = int(input('> '))

for i in range(2, x) :
    if x%i == 0 :
        print('Morakab.')
        break 
else :
    print('aval.')

#       الگوریتم سوم        #
x = int(input('> '))

for i in range(2, x) :
    if x%i == 0 :
        print('Morakab.')
        exit() 
print('aval.')