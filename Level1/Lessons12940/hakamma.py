#12940 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    max_answer = 0
    min_answer = 0
    if n >= m:
        for i in range(1,n+1):
            if n % i == 0 and m % i == 0:
                max_answer = i
        answer.append(max_answer)
    elif n < m:
        for j in range(1,m+1):
            if n % j == 0 and m % j == 0:
                max_answer = j
        answer.append(max_answer)
    min_answer = n * m / max_answer
    answer.append(min_answer)
    return answer