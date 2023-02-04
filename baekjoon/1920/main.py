def solution():
    str_n = input()
    str_list_n = input()
    str_m = input()
    str_list_m = input()

    n = int(str_n)
    list_n = [int(i) for i in str_list_n.split(' ')]
    m = int(str_m)
    list_m = [int(i) for i in str_list_m.split(' ')]

    list_n.sort()

    def binarySearch(left, right, value):
        while left <= right:
            mid = left + ((right - left + 1) // 2)

            item = list_n[mid]

            if item == value:
                return 1
            elif item > value:
                left, right = left, mid-1
            else:
                left, right = mid+1, right

        return 0

    for value in list_m:
        print(binarySearch(0, n-1, value))


solution()
