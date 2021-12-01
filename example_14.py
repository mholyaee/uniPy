import os
os.system('cls')

# علی تازه از سفر برگشته و به دوستش مقداری پول (به ریال) بدهکاره !
# با فرض اینکه علی فقط سه ارز دلار , پوند و یورو داره, برنامه ای بنویسید که مشخش کنه به چند روش میتونه بدهیشو به دوستش پرداخت کنه.
# نکته : درخط اول مقدار بدهی به ریال, در خط دوم تعداد اسکناس های هر ارز و در خط سوم ارزش ریالی هر ارز از کاربر دریافت شود.

bedehi = int(input('> ')) # 100000
a, b, c = input('> ').split(' ') # 2 1 1
a = int(a)
b = int(b)
c = int(c)
A, B, C = input('> ').split(' ') # 50000 70000 30000
A = int(A)
B = int(B)
C = int(C)

counter = 0

for i in range(a+1) :
    for j in range(b+1):
        for k in range(c+1):
            if i*A + j*B + k*C == bedehi :
                counter+=1
print(counter) # 2