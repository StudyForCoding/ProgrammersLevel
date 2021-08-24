#12928 약수의 합

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    return answer