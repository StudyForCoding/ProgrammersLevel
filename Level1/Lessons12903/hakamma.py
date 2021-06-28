가운데 글자 찾기

def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        return s[(len(s)//2)-1:(len(s)//2)+1] // index로 접근
    else:
        return s[len(s)//2]
    return answer