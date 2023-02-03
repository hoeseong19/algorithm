class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ''

        list2_zigzag_c = [[] for _ in range(numRows)]

        divider = max(1, numRows * 2 - 2)

        for index, c in enumerate(s):
            list_index = index % divider

            if list_index >= numRows:
                list_index -= numRows
                list_index += 2
                list_index = -list_index

            list2_zigzag_c[list_index].append(c)

        answer = ''.join([''.join(list_zigzag_c)
                         for list_zigzag_c in list2_zigzag_c])

        return answer


print(Solution().convert(s="PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR")
print(Solution().convert(s="PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI")
print(Solution().convert(s="A", numRows=1) == "A")
