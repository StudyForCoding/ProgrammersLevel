#12951 JadenCase ���ڿ� �����

def solution(s):
    answer = ''
    num = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            num = i+1
        elif i == num:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer