from typing import Optional
from leetcode.utils.list_node import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


solution = Solution()

print(solution.middleNode(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))) == ListNode(3, ListNode(4, ListNode(5))))
print(solution.middleNode(ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))) == ListNode(4, ListNode(5, ListNode(6))))
