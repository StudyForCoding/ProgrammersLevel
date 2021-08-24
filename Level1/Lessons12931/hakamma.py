#12931 자릿수 더하기

def solution(n):
    answer = 0
    n_number = str(n)
    for i in range(len(n_number)):
        answer += int(n_number[i])
    return answer