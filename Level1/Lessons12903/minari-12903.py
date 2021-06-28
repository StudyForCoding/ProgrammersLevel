def solution(s):
    answer = ''
    s = list(s)
    remainder = len(s)//2
    if len(s)%2 == 0:
        answer += s[remainder-1]
        answer += s[remainder]
    else:
        answer += s[remainder]
    return answer

#s = 리스트로 전환
#if len(s)%2 == 0: return s[s//2],s[(s//2)-1]
#if len(s)%2 != 0: return s[s//2]



