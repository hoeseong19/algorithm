LIST_WEEKDAY = ['SUN','MON','TUE','WED','THU','FRI','SAT']
COUNT_WEEKDAY = 7
INDEX_INITIAL_WEEKDAY = 5

LIST_LAST_DAY_IN_LEAP_YEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

INITIAL_MONTH = 1
INITIAL_DAY = 1

def getDifferenceDays(target_month, target_day):
    difference_days = 0

    index_target_month = target_month - 1

    for index_month in range(index_target_month):
        difference_days += LIST_LAST_DAY_IN_LEAP_YEAR[index_month]

    difference_days += target_day

    difference_days -= 1

    return difference_days

def solution(a, b):
    answer = ''

    difference_days = getDifferenceDays(a, b)

    index_weekday = (difference_days + INDEX_INITIAL_WEEKDAY) % COUNT_WEEKDAY

    answer = LIST_WEEKDAY[index_weekday]

    return answer

print(solution(5, 24) == "TUE")