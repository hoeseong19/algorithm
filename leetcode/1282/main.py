from typing import List, Dict
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []

        dict_groupSize_TO_count = defaultdict(int)
        dict_groupSize_TO_list:Dict[int, List[int]] = {}

        for personIndex, groupSize in enumerate(groupSizes):
            count = dict_groupSize_TO_count.get(groupSize, 0)

            if count == 0:
                dict_groupSize_TO_list[groupSize] = []

            dict_groupSize_TO_list[groupSize].append(personIndex)

            next_count = (count + 1) % groupSize

            if next_count == 0:
                answer.append(dict_groupSize_TO_list[groupSize])

            dict_groupSize_TO_count[groupSize] = next_count

        return answer
    

print(Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3]) == [[5],[0,1,2],[3,4,6]])
print(Solution().groupThePeople(groupSizes = [2,1,3,3,3,2]) == [[1],[0,5],[2,3,4]])