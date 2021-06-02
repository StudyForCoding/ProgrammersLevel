# 약수의 개수와 덧셈
def DivisorCount(n):
    i, cnt = 1,0
    divisor = []
    while i * i <= n:
        if n % i == 0:
            divisor.append(i)
            if i * i != n:
                divisor.append(n//i)
                cnt += 1
            cnt += 1
        i += 1
    return n if cnt % 2 == 0 else -n
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += DivisorCount(i)
    return answer

'''
테스트 1 〉	통과 (2.82ms, 10.3MB)
테스트 2 〉	통과 (0.65ms, 10.2MB)
테스트 3 〉	통과 (1.20ms, 10.1MB)
테스트 4 〉	통과 (0.26ms, 10.2MB)
테스트 5 〉	통과 (2.71ms, 10.2MB)
테스트 6 〉	통과 (0.28ms, 10.2MB)
테스트 7 〉	통과 (0.17ms, 10.2MB)
'''