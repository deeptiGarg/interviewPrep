# Longest Palindromic substring

def findSubstringPalind(inputStr):
    n = len(inputStr)
    table = [[False for i in range(n)] for j in range(n)]
    maxLength = 0

    maxLength = 1
    for i in range(n):
        table[i][i] = True

    # check for substring of length 2 
    start = 0
    i = 0   
    while i < n-1:
        if inputStr[i] == inputStr[i+1]:
            table[i][i+1] = True
            maxLength = 2
            start = i
        i = i+1

    k = 3
    while k <= n:
        i = 0
        while i < (n-k+1):
            j = i + k - 1
            if table[i+1][j-1] and inputStr[i]==inputStr[j]:
                table[i][j] = True
                maxLength = k
                start = i
            i = i + 1
        k = k +1 
    
    print('max substring palind = {0}, length = {1}'.format(inputStr[start:start+maxLength], maxLength))

findSubstringPalind('geekeg')