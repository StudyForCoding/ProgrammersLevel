#12949 Çà·ÄÀÇ °ö¼À

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            mul_result = 0
            for k in range(len(arr1[0])):
                mul_result += arr1[i][k] * arr2[k][j]
            row.append(mul_result)
        answer.append(row)
    return answer