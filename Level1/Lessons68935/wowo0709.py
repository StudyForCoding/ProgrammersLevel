def solution(n):
    s = []
    while n:
        s.append(n%3)
        n //= 3
    answer,i = 0,1
    while s:
        answer += s.pop() * i
        i *= 3
    return answer