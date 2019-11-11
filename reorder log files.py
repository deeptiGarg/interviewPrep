
def reorderlogs(logs) -> list:
    logs.sort(key = compare_key)
    return logs

def compare_key(a):
    content = a.split(' ')
    if content[1].isalpha():
        return ('a',content[1:], content[0])
    return ('b',)

def compare_2_lists(a,b):
    a = a.split(' ')
    b = b.split(' ')
    lenA = len(a)
    lenB = len(b)
    equal = 0
    if lenA == lenB:
        for i in range(1, lenA):
            if a[i] > b[i]:
                equal = 1
                break
            if a[i] < b[i]:
                equal = -1
                break
        if equal == 0:
            if(a[0] > b[0]):
                equal = 1
            else:
                equal = -1

    if lenA > lenB:
        for i in range(1, lenB):
            if a[i] > b[i]:
                equal = 1
                break
            if a[i] < b[i]:
                equal = -1
                break
        if equal == 0:
            equal = 1
    
    if lenA < lenB:
        for i in range(1, lenA):
            if a[i] < b[i]:
                equal = -1
                break
            if a[i] > b[i]:
                equal = 1
                break
        if equal == 0:
            equal = -1
    return equal
            

if __name__ == '__main__':
    arrlist = ['a1 9 2 3 1','g1 act car','zo4 4 7','ab1 off key dog','a8 act zoo']
    print(reorderlogs(arrlist))