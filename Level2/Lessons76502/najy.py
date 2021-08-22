#괄호 회전하기
from collections import deque

str_list = None

def check():
    global str_list
    stack = []

    for _str in str_list:
        if _str in ('[', '(', '{'): stack.append(_str)
        else:
            if not stack: return False
            x = stack.pop()
            if _str == ']' and x != '[': return False
            elif _str == ')' and x != '(': return False
            elif _str == '}' and x != '{': return False
    
    if stack: return False
    return True

def solution(s):
    global str_list
    answer = 0
    for i in range(len(s)):
        str_list = deque(s)
        str_list.rotate(-i)
        if check(): answer += 1

    return answer
'''
테스트 1 〉	통과 (13.54ms, 10.2MB)
테스트 2 〉	통과 (10.11ms, 10.4MB)
테스트 3 〉	통과 (10.03ms, 10.3MB)
테스트 4 〉	통과 (11.94ms, 10.2MB)
테스트 5 〉	통과 (26.95ms, 10.2MB)
테스트 6 〉	통과 (14.38ms, 10.2MB)
테스트 7 〉	통과 (17.29ms, 10.3MB)
테스트 8 〉	통과 (21.42ms, 10.3MB)
테스트 9 〉	통과 (39.97ms, 10.3MB)
테스트 10 〉	통과 (51.04ms, 10.3MB)
테스트 11 〉	통과 (79.73ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
'''