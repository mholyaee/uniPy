import os
os.system('cls')

# برنامه ای بنویسید که دو لیست از اجناس و قیمت آنها را بر اساس قیمت و اسم مرتب کند
# دو تابع برای این کار در نظر بگیرید
# نکته : اندیس هر مقدار از لیست قیمت برای کالای با همان اندیس در لیست اجناس میباشد که باید هردو لیست بر اساس تغییرات مرتب شوند

def sortBynum(name_list, price_list) :
    for temp in range(len(price_list)-1) :
        for i in range(len(price_list)-1) :
            if price_list[i] > price_list[i+1]:
                price_list[i], price_list[i+1] = price_list[i+1], price_list[i]
                name_list[i], name_list[i+1] = name_list[i+1], name_list[i]

def sortByname(name_list, price_list) :
    for temp in range(len(name_list)-1) :
        for i in range(len(name_list)-1) :
            if name_list[i] > name_list[i+1]:
                price_list[i], price_list[i+1] = price_list[i+1], price_list[i]
                name_list[i], name_list[i+1] = name_list[i+1], name_list[i]


name_list = ['pen', 'apple', 'book', 'notebook']
price_list = [2500, 3600, 1200, 3750]
sortByname(name_list, price_list)

print(name_list)
print(price_list)







