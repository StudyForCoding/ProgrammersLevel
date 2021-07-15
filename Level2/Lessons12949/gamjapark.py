# 행렬의 곱셈

import numpy as np
def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = np.dot(arr1, arr2).tolist()
    return answer
    
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.53ms, 27.3MB)
테스트 2 〉	통과 (1.48ms, 28.2MB)
테스트 3 〉	통과 (2.45ms, 28.8MB)
테스트 4 〉	통과 (0.58ms, 27.8MB)
테스트 5 〉	통과 (1.18ms, 28.3MB)
테스트 6 〉	통과 (0.77ms, 28.5MB)
테스트 7 〉	통과 (0.45ms, 27.5MB)
테스트 8 〉	통과 (0.08ms, 27.8MB)
테스트 9 〉	통과 (0.07ms, 28MB)
테스트 10 〉	통과 (1.98ms, 28.2MB)
테스트 11 〉	통과 (0.22ms, 27.6MB)
테스트 12 〉	통과 (0.09ms, 27.5MB)
테스트 13 〉	통과 (1.39ms, 28.4MB)
테스트 14 〉	통과 (1.68ms, 28.4MB)
테스트 15 〉	통과 (0.68ms, 28MB)
테스트 16 〉	통과 (0.62ms, 28.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
    

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            tmp_sum = 0
            for k in range(len(arr1[0])):
                tmp_sum += (arr1[i][k] * arr2[k][j])
            tmp.append(tmp_sum)
        answer.append(tmp)
    return answer
    
    
'''
채점을 시작합니다.정확성  테스트
테스트 1 〉통과 (3.30ms, 10.3MB)
테스트 2 〉통과 (54.93ms, 10.8MB)
테스트 3 〉통과 (59.77ms, 11.4MB)
테스트 4 〉통과 (1.71ms, 10.3MB)
테스트 5 〉통과 (40.36ms, 11MB)
테스트 6 〉통과 (23.34ms, 11.1MB)
테스트 7 〉통과 (1.65ms, 10.3MB)
테스트 8 〉통과 (0.85ms, 10.3MB)
테스트 9 〉통과 (0.63ms, 10.2MB)
테스트 10 〉통과 (42.27ms, 10.7MB)
테스트 11 〉통과 (4.41ms, 10.3MB)
테스트 12 〉통과 (1.11ms, 10.2MB)
테스트 13 〉통과 (30.27ms, 11MB)
테스트 14 〉통과 (61.05ms, 11.1MB)
테스트 15 〉통과 (19.21ms, 10.6MB)
테스트 16 〉통과 (5.75ms, 10.8MB)
채점 결과정확성: 100.0
합계: 100.0 / 100.0
'''
