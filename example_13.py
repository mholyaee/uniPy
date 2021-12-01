import os
os.system('cls')

# تابعی تعریف کنید که تعدادی نام دانشجو دریافت و برعکس ترتیب ورودی نمایش دهد.


def get_names(count) :
    my_names = list()
    for i in range(count) :
        temp = input('> name :')
        my_names.append(temp)
    for i in range(len(my_names)-1, -1, -1):
        print(my_names[i])


count = int(input('> enter the count of students :'))
get_names(count)