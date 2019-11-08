#this code computes square root of a number without sqrt function.
## Find square root of a number using binary search

def compute_square_root(num):
    start = 0
    end = num
    while (start<end):
        mid = (start + end)//2
        if mid*mid == num:
            sqrt = mid
        elif mid*mid > num:
            end = mid - 1
        elif mid*mid < num:
            start = mid + 1
            sqrt = mid
    dec = 1
    fact = 0.1
    sqrt += fact
    while(dec<=4):
        if sqrt*sqrt < num:
            sqrt += fact
        elif sqrt*sqrt > num:
            sqrt -= fact
            fact = fact /10
            sqrt += fact
            dec += 1
    return sqrt

if __name__ == '__main__':
    print(compute_square_root(38))
