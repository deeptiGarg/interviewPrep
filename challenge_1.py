'''
Find longest word in dictionary that is a subsequence of a given string
'''
from collections import defaultdict

def find_substring(D_list, S_str):
    S_dict = defaultdict(list)
    for idx, ch in enumerate(S_str):
        S_dict[ch].append(idx)
    max_sub_len = 0
    max_sub = ""    
    for word in D_list:
        curr_pos = -1
        curr_sub = []
        if len(word)>max_sub_len:
            for ch in word:
                if ch in S_dict:
                    for ch_idx in S_dict[ch]:
                        if ch_idx>curr_pos:
                            curr_sub.append(ch)
                            curr_pos = ch_idx
                            break
        if(len(curr_sub)>max_sub_len):
            max_sub = "".join(curr_sub)
            max_sub_len = len(max_sub)
    return max_sub

if __name__=='__main__':
    D = ["able", "ale", "apple", "bale", "kangaroo","aplpes"]
    S = "abpppleepes"
    print(find_substring(D, S))