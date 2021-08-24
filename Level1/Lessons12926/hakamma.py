#12926 시저 암호

def solution(s, n):
    low_char = "abcdefghijklmnopqrstuvwxyz"
    up_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low_char:
            ind = low_char.find(char)+n # low 문자열에서 찾은 해당 알파벳 인덱스 + n
            answer += low_char[ind%26] # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능
        elif char in up_char:
            ind = up_char.find(char)+n
            answer += up_char[ind%26]
        else:
            answer += " "
    return answer