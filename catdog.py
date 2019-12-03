# Return True if the string "cat" and "dog" appear the same number of times in the given string.

'''
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True'''


def cat_dog(str):
    count_c = 0
    count_d = 0
    i = 0
    while(i < len(str)-2):
        if str[i:i+2] == 'cat':
            count_c += 1
            i += 3
        elif str[i:i+2] == 'dog':
            count_d += 1
            i += 3
        else:
            i = i+1
    print(count_c)
    print(count_d)
    if count_c == count_d:
        return True
    return False


print(cat_dog('catcat'))
