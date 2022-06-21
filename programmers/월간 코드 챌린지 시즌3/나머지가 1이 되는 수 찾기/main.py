def getListDivisor(number):
    list_divisor = []
    
    # 1 제외
    for divisor in range(2, number+1):
        if number % divisor == 0:
            list_divisor.append(divisor)
    
    return list_divisor

def solution(n):
    answer = 0

    list_divisor = getListDivisor(n-1)

    answer = min(list_divisor)

    return answer