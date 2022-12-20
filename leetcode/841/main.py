from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length_rooms = len(rooms)

        list_is_visit = [False for _ in range(length_rooms)]

        def dfs(room_nubmer):
            list_is_visit[room_nubmer] = True

            list_key = rooms[room_nubmer]

            while list_key:
                dfs(list_key.pop())

        dfs(0)

        return all(list_is_visit)


solution = Solution()

print(solution.canVisitAllRooms(rooms=[[1], [2], [3], []]) == True)
print(solution.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]) == False)
