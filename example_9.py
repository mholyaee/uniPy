import os 
os.system('cls')

# برنامه ای بنویسید که تعداد مشخصی نمره از کاربر دریافت کرده و به همه آنها چنان بطور مساوی اضافه کند که بالاترین نمره کلاس 20 شود

n = int(input('> count of students :'))

glare = float(input('> '))
A = [glare,]
max = glare

for i in range(n-1):
    glare = float(input('> '))
    A.append(glare)
    if glare > max : max = glare


temp = 20 - max
for i in range(n):
    A[i] = A[i] + temp

print(A)