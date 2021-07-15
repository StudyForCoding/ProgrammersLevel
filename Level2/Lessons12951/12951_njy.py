#JadenCase 문자열 만들기
def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] == '':
                answer+=' '
        else:
            if s[i][0].isalpha():
                answer += s[i][0].upper()
            else:
                    answer += s[i][0]
            for j in range(1,len(s[i])):
                answer += s[i][j].lower()
            answer += ' '
        
    return answer[:-1]

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.4MB)
테스트 15 〉	통과 (0.05ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
'''