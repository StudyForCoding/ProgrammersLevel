#12934 정수 제곱근 판별

def solution(n):
    answer = 0
    a = n**(1/2)
    if int(a) == a:
        answer = (a+1)**2
    else:
        answer = -1
    return answer