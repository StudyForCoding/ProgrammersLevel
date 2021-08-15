# 괄호 회전하기

def is_correct(parenthesis):
    s = ['']
    for p in parenthesis:
        if p in [')','}',']']:
            if s[-1]+p in ['()','{}','[]']: s.pop()
            else: break
        else: s.append(p)
    # 맞지 않는 '닫는 괄호'가 없고, 남는 '여는 괄호'가 없을 때만 True
    else: return True if len(s) == 1 else False 
    return False

def solution(s):
    # return sum([is_correct(s[i+1:]+s[:i+1]) for i in range(len(s))])
    ans = 0
    for i in range(len(s)): ans += is_correct(s[i+1:]+s[:i+1])
    return ans 


'''
정확성  테스트
테스트 1 〉	통과 (8.12ms, 10.3MB)
테스트 2 〉	통과 (4.09ms, 10.2MB)
테스트 3 〉	통과 (3.95ms, 10.2MB)
테스트 4 〉	통과 (5.90ms, 10.2MB)
테스트 5 〉	통과 (21.14ms, 10.2MB)
테스트 6 〉	통과 (8.11ms, 10.2MB)
테스트 7 〉	통과 (11.25ms, 10.3MB)
테스트 8 〉	통과 (15.56ms, 10.4MB)
테스트 9 〉	통과 (31.70ms, 10.2MB)
테스트 10 〉	통과 (46.02ms, 10.4MB)
테스트 11 〉	통과 (66.83ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''