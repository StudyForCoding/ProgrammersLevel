def solution(s):
    answer = ''
    answer = s[len(s)//2-1 : len(s)//2 + 1]
    if len(s) % 2 == 1:
        answer = answer[-1]
    return answer