# a = [[2,4,6],[3,5,7]] ->
# a = [2,4,6,3,5,7]

''' a = [[[[ 4,  6,  7,  65],
         [ 5,  77,  4,  5]],

        [[ 7,  12,  33,  03],
         [ 36,  77,  55,  45]],

        [[ 67,  2,  2,  55],
         [ 24,  75,  33,  6]]]]'''

def flatten_array(arr):
    new_arr = []
    for row in arr:
        for i in row:
            if type(i) == list:
                new_arr.extend(flatten_array(i))
            else:
                new_arr.append(i)
    return new_arr

if __name__ == '__main__':

    print(flatten_array([[[[ 4,  6,  7,  65],
         [ 5,  77,  4,  5]],[[ 7,  12,  33,  3],[ 36,  77,  55,  45]],[[ 67,  2,  2,  55],
         [ 24,  75,  33,  6]]]]))