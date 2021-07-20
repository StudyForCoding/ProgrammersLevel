#n진수 게임

def dec2n(n, num):
    arr = "0123456789ABCDEF"
    ret = ''
    if num == 0:
        return '0'
    while num > 0:
        ret = arr[num % n] + ret
        num = num // n
    return ret

def solution(n, t, m, p):
    answer = ''
    string = ''
    max_num = t*m
    
    for i in range(max_num):
        string += dec2n(n, i)
        
    for s in range(p-1, max_num, m):
        answer += string[s]

    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.89ms, 10.2MB)
테스트 6 〉	통과 (0.80ms, 10.2MB)
테스트 7 〉	통과 (0.75ms, 10.3MB)
테스트 8 〉	통과 (0.33ms, 10.3MB)
테스트 9 〉	통과 (0.32ms, 10.2MB)
테스트 10 〉	통과 (0.31ms, 10.2MB)
테스트 11 〉	통과 (0.32ms, 10.3MB)
테스트 12 〉	통과 (0.26ms, 10.3MB)
테스트 13 〉	통과 (0.30ms, 10.2MB)
테스트 14 〉	통과 (60.49ms, 10.5MB)
테스트 15 〉	통과 (63.01ms, 10.5MB)
테스트 16 〉	통과 (56.82ms, 10.5MB)
테스트 17 〉	통과 (4.39ms, 10.2MB)
테스트 18 〉	통과 (2.54ms, 10.2MB)
테스트 19 〉	통과 (1.01ms, 10.1MB)
테스트 20 〉	통과 (2.38ms, 10.2MB)
테스트 21 〉	통과 (13.31ms, 10.3MB)
테스트 22 〉	통과 (9.25ms, 10.3MB)
테스트 23 〉	통과 (19.00ms, 10.3MB)
테스트 24 〉	통과 (67.84ms, 10.5MB)
테스트 25 〉	통과 (77.11ms, 10.8MB)
테스트 26 〉	통과 (8.52ms, 10.2MB)
"""