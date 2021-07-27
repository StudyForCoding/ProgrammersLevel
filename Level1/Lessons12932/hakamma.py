#12932 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    n_number = str(n)
    for i in range(len(n_number)):
        answer.append(int(n_number[len(n_number)-i-1]))
    return answer