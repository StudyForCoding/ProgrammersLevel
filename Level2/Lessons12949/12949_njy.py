#행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr2)):
                tmp += arr1[i][k] * arr2[k][j]
            result.append(tmp)
        answer.append(result) 
        
    return answer

'''
테스트 1 〉	통과 (3.25ms, 10.4MB)
테스트 2 〉	통과 (56.06ms, 11.1MB)
테스트 3 〉	통과 (59.93ms, 11.4MB)
테스트 4 〉	통과 (1.84ms, 10.3MB)
테스트 5 〉	통과 (40.11ms, 11.1MB)
테스트 6 〉	통과 (24.92ms, 11MB)
테스트 7 〉	통과 (1.76ms, 10.3MB)
테스트 8 〉	통과 (0.90ms, 10.2MB)
테스트 9 〉	통과 (0.81ms, 10.4MB)
테스트 10 〉	통과 (43.19ms, 10.6MB)
테스트 11 〉	통과 (4.82ms, 10.3MB)
테스트 12 〉	통과 (1.11ms, 10.3MB)
테스트 13 〉	통과 (31.98ms, 10.8MB)
테스트 14 〉	통과 (61.16ms, 11.1MB)
테스트 15 〉	통과 (18.88ms, 10.7MB)
테스트 16 〉	통과 (6.67ms, 10.7MB)
'''