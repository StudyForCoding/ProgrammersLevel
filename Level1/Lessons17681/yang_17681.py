# 비밀지도
def solution(n, arr1, arr2):
    answer = []
    arr1_copy = []
    arr2_copy = []
    for idx in range(n):
        bin1 = bin(arr1[idx])
        bin2 = bin(arr2[idx])
        bin1 = bin1[2:]
        bin2 = bin2[2:]
        while(len(bin1) < n):
            bin1 = '0' + bin1
        while(len(bin2) < n):
            bin2 = '0' + bin2

        bin1 = [int(i) for i in list(bin1)]
        bin2 = [int(i) for i in list(bin2)]
        arr1_copy.append(list(bin1))
        arr2_copy.append(list(bin2))


    print(arr1_copy)
    print(arr2_copy)
    

    for y in range(n):
        tmp = []
        for x in range(n):
            tmp.append(int(arr1_copy[y][x] or arr2_copy[y][x]))
        answer.append(tmp)
    result = []
    for y in range(n):
        tmp = []
        for x in range(n):
            if answer[y][x] == 1:
                tmp.append('#')
            else:
                tmp.append(' ')
        result.append(''.join(tmp))
    return result
# 테스트 1 〉	통과 (0.15ms, 10.4MB)
# 테스트 2 〉	통과 (0.37ms, 10.4MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.16ms, 10.4MB)
# 테스트 5 〉	통과 (0.11ms, 10.4MB)
# 테스트 6 〉	통과 (0.21ms, 10.4MB)
# 테스트 7 〉	통과 (0.10ms, 10.5MB)
# 테스트 8 〉	통과 (0.08ms, 10.4MB)