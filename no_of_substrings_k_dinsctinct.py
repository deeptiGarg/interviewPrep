def getsub(strinpt, k):
    n = len(strinpt)
    count = 0
    for i in range(n-k+1):
        j = i + 1
        unq = [strinpt[i]]
        while j < n:
            if len(unq) == k:
                if strinpt[j] in unq:
                    count = count + 1
                    j = j + 1
                else:
                    break
            elif len(unq) > k:
                break
            elif len(unq) < k:
                if strinpt[j] in unq:
                    j = j + 1
                else:
                    unq.append(strinpt[j])
                    j = j + 1
                    if len(unq) == k:
                        count = count + 1
    return count


if __name__ == '__main__':
    print(getsub('abc',2))


            