# 시저암호

def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
                answer += " "
                continue
        code = ord(i) + n
        if i.islower():     #소문자
            if code > 122:
                code -= 26
        else:               #대문자
            if code > 90:
                code -= 26
        answer += chr(code)
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (2.13ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0

'''
