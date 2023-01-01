class Solution:
    def convertStringToIndex(self, list_string):
        dict_s = {}
        list_index_s = []

        s_index_counter = 0
        for c in list_string:
            s_index = dict_s.get(c)
            if s_index is None:
                dict_s[c] = s_index_counter

                s_index = s_index_counter

                s_index_counter += 1

            list_index_s.append(s_index)

        return list_index_s

    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.convertStringToIndex(pattern) == self.convertStringToIndex(s.split(' '))


print(Solution().wordPattern(pattern="abba", s="dog cat cat dog") == True)
print(Solution().wordPattern(pattern="abba", s="dog cat cat fish") == False)
print(Solution().wordPattern(pattern="aaaa", s="dog cat cat dog") == False)
