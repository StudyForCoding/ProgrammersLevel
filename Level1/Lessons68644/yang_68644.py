def solution(numbers):
    answer = []
    idx = len(numbers)
    for x in range(idx):
        for y in range(x+1,idx):
            answer.append(numbers[x] + numbers[y])
    answer = list(set(answer))
    answer.sort()
    return answer