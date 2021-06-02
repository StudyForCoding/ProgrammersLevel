import itertools

def solution(numbers):
    answer = set([])
    for x, y in list(itertools.combinations(numbers,2)):
        answer.add(x+y)
    answer = list(answer)
    answer.sort()
    return answer