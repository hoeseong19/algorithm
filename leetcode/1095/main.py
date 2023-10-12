from typing import Iterable, List

"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""


class MountainArray:
    def __init__(self, _list: List[int]):
        self._list = _list

    def get(self, index: int) -> int:
        return self._list[index]

    def length(self) -> int:
        return len(self._list)


class Condition:
    def __init__(self, arr_s: int, arr_e: int, mountain_arr: "MountainArray"):
        self.arr_s = arr_s
        self.arr_e = arr_e
        self.mountain_arr = mountain_arr

    def setCurIndex(self, cur_index: int):
        self.cur_index = cur_index

    def indexToLeft(self):
        pass

    def indexToRight(self):
        pass

    def getNextLeftPositions(self, s: int) -> Iterable[int]:
        return s, max(self.cur_index - 1, s)

    def getNextRightPositions(self, e: int) -> Iterable[int]:
        return min(self.cur_index + 1, e), e


class PeakCondition(Condition):
    def indexToLeft(self):
        prev_index = max(self.cur_index - 1, self.arr_s)
        next_index = min(self.cur_index + 1, self.arr_e)

        return self.mountain_arr.get(prev_index) > self.mountain_arr.get(self.cur_index) >= self.mountain_arr.get(next_index)

    def indexToRight(self):
        prev_index = max(self.cur_index - 1, self.arr_s)
        next_index = min(self.cur_index + 1, self.arr_e)

        return self.mountain_arr.get(prev_index) <= self.mountain_arr.get(self.cur_index) < self.mountain_arr.get(next_index)


class LeftHillCondition(Condition):
    def __init__(self, arr_s: int, arr_e: int, mountain_arr: "MountainArray", target: int):
        super().__init__(arr_s, arr_e, mountain_arr)
        self.target = target

    def indexToLeft(self):
        return self.mountain_arr.get(self.cur_index) > self.target

    def indexToRight(self):
        return self.mountain_arr.get(self.cur_index) < self.target


class RightHillCondition(Condition):
    def __init__(self, arr_s: int, arr_e: int, mountain_arr: "MountainArray", target: int):
        super().__init__(arr_s, arr_e, mountain_arr)
        self.target = target

    def indexToLeft(self):
        return self.mountain_arr.get(self.cur_index) < self.target

    def indexToRight(self):
        return self.mountain_arr.get(self.cur_index) > self.target


class Solution:
    def binarySearch(self, arr_s: int, arr_e: int, condition: Condition) -> int:
        s, e = arr_s, arr_e

        condition.setCurIndex(cur_index=(arr_s + arr_e) // 2)

        while s != e:
            # to left
            if condition.indexToLeft():
                s, e = condition.getNextLeftPositions(s)
            # to right
            elif condition.indexToRight():
                s, e = condition.getNextRightPositions(e)
            # on target
            else:
                break

            condition.setCurIndex(cur_index=(s + e) // 2)

        condition.setCurIndex(cur_index=(s + e) // 2)

        return condition.cur_index

    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        answer = -1

        arr_s, arr_e = 0, mountain_arr.length() - 1

        peakIndex = self.binarySearch(arr_s, arr_e, PeakCondition(arr_s, arr_e, mountain_arr))

        leftTargetIndex = self.binarySearch(arr_s, peakIndex, LeftHillCondition(arr_s, peakIndex, mountain_arr, target))

        rightTargetIndex = self.binarySearch(peakIndex, arr_e, RightHillCondition(peakIndex, arr_e, mountain_arr, target))

        if mountain_arr.get(rightTargetIndex) == target:
            answer = rightTargetIndex

        if mountain_arr.get(leftTargetIndex) == target:
            answer = leftTargetIndex

        return answer


print(Solution().findInMountainArray(target=3, mountain_arr=MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2)
print(Solution().findInMountainArray(target=3, mountain_arr=MountainArray([0, 1, 2, 4, 2, 1])) == -1)
print(Solution().findInMountainArray(target=5, mountain_arr=MountainArray([1, 5, 2])) == 1)
