import os
os.system('cls')

# برنامه ای بنویسید که یک فایل متنی باز کرده و یک لیستی از کلمات اون متن نمایش بده
# کلمات میتونن با کاربر های فاصله, کاما, ادساین و نقطه از هم جدا بشن.

string = open('file.txt', 'r').read().replace('.', ' ').replace(',', ' ').replace('@', ' ').replace('\n', ' ').replace('   ', ' ').replace('  ', ' ').split()

print(string)