#올바른 괄호
def solution(s):
    left = 0
    right = 0
    for i in range(len(s)):
        if s[i]=='(':
            left += 1
        else:
            right += 1

        if right>left:
            return False
    if right!=left:
        return False
    return True

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (9.56ms, 10.2MB)
테스트 2 〉	통과 (10.17ms, 10.3MB)
'''