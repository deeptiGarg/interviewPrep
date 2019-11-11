from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_sub_len = 0
        start = 0
        for i in range(n):
            dict_sub = defaultdict(int)
            sub_length = 0
            for j in range(i,n):
                if dict_sub[s[j]] >= 1:
                    break
                else:
                    dict_sub[s[j]] += 1
                    sub_length += 1
            if max_sub_len < sub_length:
                max_sub_len = sub_length
                start = i
        return max_sub_len
    
    # Runs in O(n) time
    def ONlengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_sub_len = 0
        sub_list = []
        dict_sub = defaultdict(int)
        for i in range(n):
            sub_list.append(s[i])
            dict_sub[s[i]] += 1
            if dict_sub[s[i]] > 1:                
                while(sub_list[0]!=s[i]):
                    sub_length = len(sub_list)-1
                    if max_sub_len < sub_length:
                        max_sub_len = sub_length
                    item = sub_list.pop(0)
                    dict_sub[item] -= 1
                item = sub_list.pop(0)
                dict_sub[item] -= 1
        sub_length = len(sub_list)
        if max_sub_len < sub_length:
            max_sub_len = sub_length
        return max_sub_len

sol = Solution()
print(sol.ONlengthOfLongestSubstring("abcabcbb"))