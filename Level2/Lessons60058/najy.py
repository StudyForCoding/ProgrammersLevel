# 괄호 변환

def convert(p):
    ret = ''
    for par in p[1:-1]:
        if par == '(':
            ret += ')'
        else : ret += '('
    return ret

def solution(p):
    l,r = 0, 0 # (,) 개수 카운터
    u,v = '', '' # p를 나눠 저장할 문자열
    flag = True # 올바른 괄호 문자열 구분
    
    # 빈 문자열 -> 빈 문자열 반환
    if p == '':
        return ''
    
    # 균형잡힌 괄호 문자열 될 때 까지 인덱싱 후 스플릿
    for idx, par in enumerate(p):
        if par == '(':
            l += 1
        else : r += 1
        if r>l : flag = False
        if l == r:
            u, v = p[:idx+1], p[idx+1:]
            break
    # u가 올바른 괄호 문자열일 경우 v에 대하여 반복
    if flag:
        return u+solution(v)
    else:
        return '('+solution(v)+')'+convert(u)
    
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
테스트 15 〉	통과 (0.08ms, 10.2MB)
테스트 16 〉	통과 (0.18ms, 10.1MB)
테스트 17 〉	통과 (0.14ms, 10.2MB)
테스트 18 〉	통과 (0.24ms, 10.3MB)
테스트 19 〉	통과 (0.39ms, 10.3MB)
테스트 20 〉	통과 (0.28ms, 10.2MB)
테스트 21 〉	통과 (0.31ms, 10.2MB)
테스트 22 〉	통과 (0.16ms, 10.2MB)
테스트 23 〉	통과 (0.26ms, 10.1MB)
테스트 24 〉	통과 (0.09ms, 10.1MB)
테스트 25 〉	통과 (0.14ms, 10.3MB)
'''