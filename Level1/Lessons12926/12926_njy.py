#시저 암호

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] != ' ':
            if s[i].islower():
                answer += chr((ord(s[i])-ord('a')+n)%26 + ord('a'))
            else:
                answer += chr((ord(s[i])-ord('A')+n)%26 + ord('A'))
        else:
            answer += ' '
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.1MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (2.56ms, 10.2MB)
'''