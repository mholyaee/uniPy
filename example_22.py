import os
os.system('cls')

# تابعی برای سرچ در فایل متنی بنویسید

def search(path, word) -> bool:
    if word in open(path, 'r').read().replace('\n', ' ').split() :
        return True
    return False

def search(path, word, sensivity) -> bool :
    my_file = open(path, 'r')
    for line in my_file :
        for w in line.strip().split():
            if sensivity :
                if w == word :
                    return True
            else :
                if w.capitalize() == word.capitalize() :
                    return True
    return False