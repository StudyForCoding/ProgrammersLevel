#12915 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    a = []
    strings.sort()
    for i in strings:
        a.append(i[n])
    a.sort()
    
    for j in a:
        for k in range(len(a)):
            if j == strings[k][n]:
                answer.append(strings[k])
                strings[k] = '0'*100 # 중복방지를 위해 요소의 값 변경
    return answer