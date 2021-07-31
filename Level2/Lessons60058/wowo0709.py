# 괄호 변환
def is_correct(parentheses):
    tmp = 0
    for p in parentheses:
        if p == '(': tmp += 1
        else: tmp -= 1
        if tmp < 0: return False
    return True if tmp == 0 else False

def solution(p):
    # 1
    if not p: 
        return p
    # 2
    tmp = 0
    for i in range(len(p)):
        if p[i] == '(': tmp += 1
        else: tmp -= 1
        if tmp == 0: 
            u,v = p[:i+1],p[i+1:]
            break
    # 3
    if is_correct(u):
        return u + solution(v)
    # 4
    else:
        return '(' + solution(v) + ')' + ''.join(list(map(lambda p:'(' if p == ')' else ')', u[1:-1])))

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.2MB)
테스트 15 〉	통과 (0.11ms, 10.2MB)
테스트 16 〉	통과 (0.75ms, 10.4MB)
테스트 17 〉	통과 (0.19ms, 10.1MB)
테스트 18 〉	통과 (0.30ms, 10.2MB)
테스트 19 〉	통과 (0.48ms, 10.4MB)
테스트 20 〉	통과 (0.37ms, 10.2MB)
테스트 21 〉	통과 (0.35ms, 10.2MB)
테스트 22 〉	통과 (0.18ms, 10.2MB)
테스트 23 〉	통과 (0.36ms, 10.3MB)
테스트 24 〉	통과 (0.13ms, 10.3MB)
테스트 25 〉	통과 (0.23ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''