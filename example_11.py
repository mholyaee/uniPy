import os
os.system('cls')

# برنامه ای بنویسید که یک جدول ضرب ده در ده در خروجی چاپ کند

test = ''
for i in range(1, 11) :
    for j in range(1, 11) :
        test += str(i*j) + '\t'
    test += '\n'

print(test)