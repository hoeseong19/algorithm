from typing import Optional, List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def changeLinkedListToList(self, head: Optional[ListNode]) -> List[int]:
        list_val: List[int] = []

        if head is None:
            return []

        node = head

        while node.next:
            list_val.append(node.val)

            node = node.next

        list_val.append(node.val)

        return list_val

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_val = self.changeLinkedListToList(head)

        return list_val == list_val[::-1]


solution = Solution()

print(solution.isPalindrome(None) == False)
print(solution.isPalindrome(
    ListNode(1, ListNode(2, ListNode(2, ListNode(1))))) == True)
print(solution.isPalindrome(ListNode(1, ListNode(2))) == False)
print(solution.isPalindrome(ListNode(1, ListNode(
    2, ListNode(3, ListNode(2, ListNode(1)))))) == True)
