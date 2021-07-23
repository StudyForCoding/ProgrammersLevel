# 위장

def chooser(n,k):
    num = 1
    den = 1
    k = min(k, n-k) # nCk = nC(n-k)
    for i in range(1,k+1):
        num *= n+1-i # n*...*n-k+1
        den *= i # k!
    return num/den

def solution(clothes):
    answer = 1
    count = 0
    cats = dict()
    for cloth in clothes:
        count = cats.get(cloth[1],1)
        cats[cloth[1]] = count+1
    for cat in cats:
        answer *= chooser(cats[cat],1)
    return answer-1 # 모두 안입는 경우의 수 제외

'''
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
테스트 27 〉	통과 (0.01ms, 10.1MB)
테스트 28 〉	통과 (0.02ms, 10.2MB)
'''