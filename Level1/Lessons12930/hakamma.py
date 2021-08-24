#12930 이상한 문자 만들기

def solution(s):
    answer = ''
    new_s = s.split(' ')
    
    for char in new_s:
        for i in range(len(char)):
            if i%2 == 0:
                answer += char[i].upper()
            elif i%2 == 1:
                answer += char[i].lower()
        answer += ' '
    return answer[:-1]