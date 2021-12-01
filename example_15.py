import os
os.system('cls')

# برنامه ای بنویسید که یک فایل متنی باز کرده و تعداد خط ها, کلمات و کارکتر های اون فایل رو مشخص کنه

lines=0
words=0
chCount=0
my_file = open('file.txt', 'r')
for Line in my_file :
    lines += 1
    for word in Line.strip().split() :
        words += 1
        for ch in word :
            chCount += 1

print(words, lines, chCount)