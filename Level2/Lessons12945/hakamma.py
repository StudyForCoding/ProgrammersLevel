#12945 피보나치 수

def solution(n):
    answer = 0
    num = [0]*(n+1)
    num[1] = 1
    for i in range(2, n+1):
        num[i] = num[i-1] + num[i-2]
    answer = num[n] % 1234567
    return answer