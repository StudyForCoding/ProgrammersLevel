# 쿼드압축 후 개수 세기

arr = []
def compression(i, j, arr_len):
    count = 0
    for a in range(i,i+arr_len):
        for b in range(j, j+arr_len):
            count += arr[a][b]
    if count == arr_len * arr_len:
        return 0, 1
    elif count == 0:
        return 1, 0

    answer = [0,0]
    new_arr_len = arr_len//2
    cor = [(0,0), (0,1), (1,0), (1,1)]
    for c in cor:
        a, b = compression(i + c[0]*new_arr_len, j + c[1]*new_arr_len, new_arr_len)
        answer[0] += a
        answer[1] += b
    return answer

def solution(_arr):
    for a in _arr:
        arr.append(a)
    answer = compression(0,0, len(arr))
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (1.43ms, 10.2MB)
테스트 2 〉	통과 (0.90ms, 10.3MB)
테스트 3 〉	통과 (0.64ms, 10.2MB)
테스트 4 〉	통과 (0.16ms, 10.2MB)
테스트 5 〉	통과 (450.79ms, 12.3MB)
테스트 6 〉	통과 (151.13ms, 12.2MB)
테스트 7 〉	통과 (107.77ms, 12.2MB)
테스트 8 〉	통과 (68.02ms, 12.2MB)
테스트 9 〉	통과 (41.57ms, 12.2MB)
테스트 10 〉	통과 (78.99ms, 18.9MB)
테스트 11 〉	통과 (0.11ms, 10.4MB)
테스트 12 〉	통과 (0.14ms, 10.2MB)
테스트 13 〉	통과 (49.87ms, 12.2MB)
테스트 14 〉	통과 (377.30ms, 18.8MB)
테스트 15 〉	통과 (483.90ms, 19MB)
테스트 16 〉	통과 (172.91ms, 12.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''