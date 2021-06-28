3진법 뒤집기

def solution(n):
    result = 0
    answer = ''
    while n>=1:
        remain = n%3
        dev = n//3
        n = dev
        answer = answer + str(remain)

    for i in range(len(answer)-1,-1,-1):
        result += int(answer[i]) * (3**(len(answer)-i-1))
        

    return result