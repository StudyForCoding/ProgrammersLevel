# 최대공약수와 최소공배수

def gcd(a, b): #greatest common divisor 최대공약수
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b): #large common multiple 최소공배수
    return (a * b) // gcd(a, b)

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
'''