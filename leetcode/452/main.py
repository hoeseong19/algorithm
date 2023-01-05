from collections import Counter, defaultdict
from typing import List


class Solution:
    INDEX_POINT_START = 0
    INDEX_POINT_END = 1

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        answer = 0

        length_points = len(points)

        points.sort()

        total_counter = Counter()

        dict_coord_TO_list_index = defaultdict(list)

        for index_point, point in enumerate(points):
            total_counter += Counter(
                range(point[self.INDEX_POINT_START], point[self.INDEX_POINT_END] + 1))

            for i in range(point[self.INDEX_POINT_START], point[self.INDEX_POINT_END] + 1):
                dict_coord_TO_list_index[i].append(index_point)

        while length_points > 0:
            list_coord_and_count = total_counter.most_common(1)

            coord = list_coord_and_count[0][0]

            list_index = dict_coord_TO_list_index[coord]

            for index in list_index:
                total_counter -= Counter(range(
                    points[index][self.INDEX_POINT_START], points[index][self.INDEX_POINT_END] + 1))
                length_points -= 1

            answer += 1

        return answer


print(Solution().findMinArrowShots(
    points=[[10, 16], [2, 8], [1, 6], [7, 12]]) == 2)
print(Solution().findMinArrowShots(
    points=[[1, 2], [3, 4], [5, 6], [7, 8]]) == 4)
print(Solution().findMinArrowShots(
    points=[[1, 2], [2, 3], [3, 4], [4, 5]]) == 2)
