class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ' '.join([c[::-1] for c in s.split(' ')])

        return answer


print(Solution().reverseWords(s="Let's take LeetCode contest")
      == "s'teL ekat edoCteeL tsetnoc")
print(Solution().reverseWords(s="God Ding") == "doG gniD")
