arr = [2,3,4,7,8,10, 18]
for i in range(int(len(arr)/2)):
    temp = arr[i]
    arr[i] = arr[len(arr)-1-i]
    arr[len(arr)-1-i] = temp
print(arr)

