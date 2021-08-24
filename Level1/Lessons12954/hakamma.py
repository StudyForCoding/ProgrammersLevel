#12954 x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    for i in range(0,n):
        answer.append(x*(i+1))
    return answer