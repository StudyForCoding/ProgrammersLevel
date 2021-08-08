# 괄호 변환
def isbalance(s):
    count = 0
    for p in s:
        if p == "(":
            count += 1
        elif p == ")" and count > 0:
            count -= 1
    return not count

def divide(s):
    if s == "":
        return s
    
    bal_dic = {"(":0, ")":1}
    balance = [0, 0]
    for p in s:
        balance[bal_dic[p]] += 1
        if balance[0] == balance[1]:
            u = s[:balance[0]*2]
            v = s[balance[0]*2:]
            break
    if isbalance(u):
        return u + divide(v)

    new = ""
    u_len = len(u)
    if u_len > 2:
        tmp = u[1:-1]
        for i in range(u_len-2):
            if tmp[i] == "(":
                new += ")"
            else:
                new += "("
    return "(" + divide(v) + ")" + new

def solution(p): 
    answer = divide(p)
    return answer


'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.3MB)
테스트 14 〉	통과 (0.10ms, 10.2MB)
테스트 15 〉	통과 (0.13ms, 10.3MB)
테스트 16 〉	통과 (0.29ms, 10.3MB)
테스트 17 〉	통과 (0.23ms, 10.4MB)
테스트 18 〉	통과 (0.36ms, 10.3MB)
테스트 19 〉	통과 (0.70ms, 10.4MB)
테스트 20 〉	통과 (0.44ms, 10.3MB)
테스트 21 〉	통과 (0.46ms, 10.3MB)
테스트 22 〉	통과 (0.24ms, 10.3MB)
테스트 23 〉	통과 (0.39ms, 10.3MB)
테스트 24 〉	통과 (0.15ms, 10.3MB)
테스트 25 〉	통과 (0.27ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''