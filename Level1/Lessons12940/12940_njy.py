#최대공약수와 최소공배수
def solution(n, m):
    #두 수의 크기 비교
    if n>m:
        n,m = m,n
    #최대공약수 계산
    #1~n까지 공약수 계산
    for i in range(1, n+1):
       if n % i == 0 and m % i == 0:
            max = i
    #최소공배수 계산
    #최대공약수가 1이면 n*m 반환
    if max == 1:
       min = n*m
    #최소공배수 = 최대공약수 * n의 몫 * m의 몫
    else:
       min = max *(n // max) *(m // max)
    return [max, min]
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.1MB)
테스트 12 〉	통과 (0.20ms, 10.2MB)
테스트 13 〉	통과 (0.11ms, 10.1MB)
테스트 14 〉	통과 (0.17ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.2MB)
테스트 16 〉	통과 (0.13ms, 10.3MB)
'''