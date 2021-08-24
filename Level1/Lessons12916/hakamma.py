#12916 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    s1 = s.lower()
    pcount = 0
    ycount = 0
    for i in range(len(s1)):
        if s1[i] == 'p':
            pcount += 1
        elif s1[i] == 'y':
            ycount += 1
    if pcount == ycount:
        answer = True
    elif pcount != ycount:
        answer = False
    return answer