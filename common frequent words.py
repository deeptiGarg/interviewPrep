class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        paragraph = paragraph.replace('!',' ').replace('?',' ').replace('\'',' ').replace(',',' ').replace(';',' ').replace('.',' ')
        dict_word_Count = {}
        max_count = 0
        for ch in paragraph.split(' '):
            if ch != '' and ch.lower() not in banned:
                if ch.lower() in dict_word_Count:
                    dict_word_Count[ch.lower()] += 1
                else:
                    dict_word_Count[ch.lower()] = 1
                if max_count < dict_word_Count[ch.lower()]:
                    max_count = dict_word_Count[ch.lower()]
        result = []
        for k, v in dict_word_Count.items():
            if v == max_count:
                result.append(k)
                return k
        #print(result)
        
sol = Solution()
print(sol.mostCommonWord("Bob. hIt, baLl",["bob", "hit"]))
