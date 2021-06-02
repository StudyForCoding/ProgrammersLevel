def solution(numbers):
    answer = [False for _ in range(201)]
    N = len(numbers)
    for i in range(N):
        for j in range(i+1,N):
            num = numbers[i] + numbers[j]
            if not answer[num]:
                answer[num] = True

    return [i for i in range(201) if answer[i]]