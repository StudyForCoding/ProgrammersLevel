# 괄호 변환
def solution(p):
    counter = 0
    open_num = 0
    if not p:
        return ''
    u = ''
    v = ''
    for tmp in p:
        if tmp == '(':
            counter += 1
            u += tmp
        else:
            counter -= 1
            u += tmp
        if counter == 0:
            v = p[len(u):]
            u_flag = True
            for inner_p in u:
                if inner_p == '(':
                    open_num += 1
                else:
                    open_num -= 1
                if open_num < 0:
                    u_flag = False
            if u_flag:
                return u + solution(v)
            else:
                new_u = ''
                for i in u[1:-1]:
                    if i == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                answer = '(' + solution(v) + ')' + new_u
                return answer
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (0.01ms, 10.4MB)
# 테스트 7 〉	통과 (0.01ms, 10.4MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.05ms, 10.2MB)
# 테스트 14 〉	통과 (0.08ms, 10.3MB)
# 테스트 15 〉	통과 (0.10ms, 10.2MB)
# 테스트 16 〉	통과 (0.23ms, 10.3MB)
# 테스트 17 〉	통과 (0.23ms, 10.2MB)
# 테스트 18 〉	통과 (0.30ms, 10.4MB)
# 테스트 19 〉	통과 (0.55ms, 10.3MB)
# 테스트 20 〉	통과 (0.41ms, 10.2MB)
# 테스트 21 〉	통과 (0.46ms, 10.2MB)
# 테스트 22 〉	통과 (0.84ms, 10.2MB)
# 테스트 23 〉	통과 (0.32ms, 10.2MB)
# 테스트 24 〉	통과 (0.15ms, 10.3MB)
# 테스트 25 〉	통과 (0.25ms, 10.3MB)