#12918 문자열 다루기 기본

def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            answer = True
    return answer