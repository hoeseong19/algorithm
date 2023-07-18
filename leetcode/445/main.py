from typing import Optional


class ListNode:  # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = None

        # l1
        item_l1 = l1

        stack_l1 = []

        while item_l1:
            stack_l1.append(item_l1.val)

            item_l1 = item_l1.next

        # l2
        item_l2 = l2

        stack_l2 = []

        while item_l2:
            stack_l2.append(item_l2.val)

            item_l2 = item_l2.next

        quotient = 0

        prev_item_answer: Optional[ListNode] = None
        item_answer: ListNode = ListNode(0, next=prev_item_answer)

        while len(stack_l1) != 0 or len(stack_l2) != 0:
            num_l1 = 0
            num_l2 = 0

            item_answer: ListNode = ListNode(0, next=prev_item_answer)

            if len(stack_l1) != 0: 
                num_l1 = stack_l1.pop()
            if len(stack_l2) != 0:
                num_l2 = stack_l2.pop()

            sum_nums = num_l1 + num_l2

            num = (sum_nums + quotient) % 10

            item_answer.val = num
            item_answer.next = prev_item_answer

            quotient = (sum_nums + quotient) // 10

            prev_item_answer = item_answer

        if quotient > 0:

            item_answer: ListNode = ListNode(0, next=prev_item_answer)

            item_answer.val = quotient
            item_answer.next = prev_item_answer

        answer = item_answer

        return answer


# print(Solution().addTwoNumbers(l1=ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), l2=ListNode(
#     5, ListNode(6, ListNode(4)))) == ListNode(7, ListNode(8, ListNode(0, ListNode(7)))))
# print(Solution().addTwoNumbers(l1=ListNode(2, ListNode(4, ListNode(3))), l2=ListNode(
#     5, ListNode(6, ListNode(4)))) == ListNode(8, ListNode(0, ListNode(7))))
# print(Solution().addTwoNumbers(l1=ListNode(0), l2=ListNode(0)) == ListNode(0))
# print(Solution().addTwoNumbers(l1=ListNode(5), l2=ListNode(5)) == ListNode(1, ListNode(0)))
# print(Solution().addTwoNumbers(l1=ListNode(5, ListNode(5)), l2=ListNode(5, ListNode(5))) == ListNode(1, ListNode(1, ListNode(0))))
print(Solution().addTwoNumbers(l1=ListNode(1), l2=ListNode(9, ListNode(9))) == ListNode(1, ListNode(0, ListNode(0))))
