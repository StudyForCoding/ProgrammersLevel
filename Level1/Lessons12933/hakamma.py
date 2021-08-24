#12933 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    n_number = str(n)
    t = []
    for i in range(len(n_number)):
        t.append(int(n_number[len(n_number)-i-1]))
    
    t.sort(reverse=True)
    s=''.join(map(str,t)) # 리스트를 특정 구분자를 포함해 문자열로 변환
    answer = int(s)
    return answer