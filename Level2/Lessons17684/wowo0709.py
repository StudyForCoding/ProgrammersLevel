# [3차] 압축
from string import ascii_uppercase

def solution(msg):
    zip_dict = dict(zip(ascii_uppercase,range(1,27)))
    zip_list = []
    N,i = len(msg),0
    
    while i < N:
        for j in range(i,N):
            if msg[i:j+1] not in zip_dict:
                zip_list.append(zip_dict[msg[i:j]])
                zip_dict[msg[i:j+1]] = len(zip_dict)+1
                i = j
                break
            if j == N-1:
                zip_list.append(zip_dict[msg[i:j+1]])
                return zip_list


'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.26ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.41ms, 10.3MB)
테스트 7 〉	통과 (0.32ms, 10.2MB)
테스트 8 〉	통과 (0.42ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.33ms, 10.3MB)
테스트 11 〉	통과 (0.32ms, 10.3MB)
테스트 12 〉	통과 (0.36ms, 10.4MB)
테스트 13 〉	통과 (0.72ms, 10.3MB)
테스트 14 〉	통과 (0.62ms, 10.2MB)
테스트 15 〉	통과 (0.65ms, 10.3MB)
테스트 16 〉	통과 (0.44ms, 10.3MB)
테스트 17 〉	통과 (0.34ms, 10.3MB)
테스트 18 〉	통과 (0.13ms, 10.3MB)
테스트 19 〉	통과 (0.17ms, 10.3MB)
테스트 20 〉	통과 (0.36ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''