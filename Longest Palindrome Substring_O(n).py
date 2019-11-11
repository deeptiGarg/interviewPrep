#xyzzyabc return yzzy
#abcbx return bcb

def get_longest_substring_palin(strInput):
    i = 0
    max_length_sub = 1
    sub = ''
    while(i<n):
        #check when substring is odd
        palin_sub = get_Palin_odd(strInput, i)
        if max_length_sub < len(palin_sub):
            max_length_sub = len(palin_sub)
            sub = palin_sub

        #check when substring is even
        palin_sub = get_Palin_even(strInput, i) 
        if max_length_sub < len(palin_sub):
            max_length_sub = len(palin_sub)
            sub = palin_sub
        i = i+1
    return sub

def get_Palin_odd(strinp, center):
    pos = 1
    retSub = strinp[center]
    while(center-pos >= 0 and center+pos < len(strinp) and strinp[center-pos] == strinp[center+pos]): 
        retSub = strinp[center-pos:center+pos+1]
        pos += 1
    return retSub

def get_Palin_even(strinp, center):
    pos = 1
    center2 = center + 1
    restSub = ''
    if(center2 < len(strinp) and strinp[center]== strinp[center2]):
        restSub = strinp[center:center+1]
        while(center - pos >=0 and center + 1 +pos <len(strinp) and strinp[center-pos]== strinp[center+1+pos]):
            restSub = strinp[center - pos:center + 1 +pos+1]
            pos += 1
    return restSub

if __name__ == "__main__":
    print('hello')
    print(get_longest_substring_palin('xyzzyabc'))