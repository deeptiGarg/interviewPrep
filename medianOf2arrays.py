## Program to compute median of the combined array; given 2 sorted arrays.
# assumption 1 - Arrays can be of unequal lengths.

'''
Example:
arr1 = 2,3,4,5,8
arr2 = 1,2,5,6,9,11,13
Answer = 5
'''
import math

def get_med(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    med_index = -1
    isEven = False
    med_item = []
    # get median index of both arrays
    if (len_arr1+len_arr2) %2 == 0:
        med_index = (len_arr1+len_arr2)//2
        isEven = True
    else:
        med_index = math.ceil((len_arr1+len_arr2)/2)

    tracker_1 = 0
    tracker_2 = 0
    tracker_comb = med_index
    more_medians = True
    while(len_arr1!=0 and len_arr2!=0):
        tracker_comb -= 1
        if arr1[tracker_1] <= arr2[tracker_2]:
            if(tracker_comb == 0):
                med_item.append(arr1[tracker_1])
                if isEven and more_medians:
                    tracker_comb = 1
                    more_medians = False
                else:
                    more_medians = False
                    break
            tracker_1 += 1
            len_arr1 -= 1            
        elif arr1[tracker_1] >arr2[tracker_2]:
            if(tracker_comb == 0):
                med_item.append(arr2[tracker_2])
                if isEven and more_medians:
                    tracker_comb = 1
                    more_medians = False
                else:
                    more_medians = False
                    break
            tracker_2 += 1
            len_arr2 -= 1
    
    # If arr1 got over:
    if(len_arr1 == 0 and more_medians):
        med_item.append(arr2[tracker_2+tracker_comb-1])
        if isEven:
            med_item.append(arr2[tracker_2+tracker_comb])
    
    #If arr2 got over:
    if(len_arr2 == 0 and more_medians):
        med_item.append(arr1[tracker_1+tracker_comb-1])
        if isEven:
            med_item.append(arr1[tracker_1+tracker_comb])
    if isEven:
        median_element = sum(med_item)/2
    else:
        median_element = med_item[0]
    return median_element

if __name__=='__main__':
    arr1 = [-5, 3, 6, 12, 15]#[2, 3, 5, 8]#[2,3,4,5,8]    
    arr2 = [-12, -10, -6, -3, 4, 10]#[10, 12, 14, 16, 18, 20]#[1,2,5,6,9,11,13]
    print("Median of combined arrays = ", get_med(arr1,arr2))
    print(arr2[-2:])
    arr2d = []
    arr2d.append([1, 0, 1, 0])
    arr2d.append([1, 0, 1, 0])
    print(len(arr2d))
    print(len(arr2d[0]))