from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length_rooms = len(rooms)

        list_is_visit = [False for _ in range(length_rooms)]

        q_room = deque([0])

        while q_room:
            room_number = q_room.popleft()

            list_is_visit[room_number] = True

            list_room_number = rooms[room_number]

            while list_room_number:
                q_room.append(list_room_number.pop())

        return all(list_is_visit)


solution = Solution()

print(solution.canVisitAllRooms(rooms=[[1], [2], [3], []]) == True)
print(solution.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]) == False)
