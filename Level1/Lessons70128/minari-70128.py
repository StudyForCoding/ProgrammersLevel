def solution(a, b):
    answer = 0
    for i in range(len(a)):
        DotProduct = a[i] * b[i]
        answer += DotProduct
    return answer