#70128

def solution(a, b):
    answer = 0
    result_sum = 0
    for i in range(len(a)):
        result_sum += (int(a[i]) * int(b[i]))
    
    answer = result_sum
    return answer