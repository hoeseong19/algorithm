class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count = 0
        b_count = 0

        latest_color = ''
        count = 0

        for color in colors:

            if latest_color != color:
                if latest_color == 'A':
                    a_count = a_count + (count - 2 if count >= 3 else 0)
                if latest_color == 'B':
                    b_count = b_count + (count - 2 if count >= 3 else 0)

                count = 0

            count += 1

            latest_color = color

        if latest_color == 'A':
            a_count = a_count + (count - 2 if count >= 3 else 0)
        if latest_color == 'B':
            b_count = b_count + (count - 2 if count >= 3 else 0)

        return a_count > b_count


print(Solution().winnerOfGame(colors="AAABABB") == True)
print(Solution().winnerOfGame(colors="AA") == False)
print(Solution().winnerOfGame(colors="ABBBBBBBAAA") == False)
print(Solution().winnerOfGame(colors="AAAABBBB") == False)
