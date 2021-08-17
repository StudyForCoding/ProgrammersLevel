#이진 변환 반복하기

def solution(s):
    answer = [0,0]
    while(s!='1'):
        len1 = 0
        for num in s:
            if num == '1':
                len1 += 1
        answer[0] += 1
        answer[1] += len(s)-len1
        s = bin(len1)[2:]
    return answer
        
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (4.26ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.10ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (4.23ms, 10.3MB)
테스트 10 〉	통과 (6.08ms, 10.3MB)
테스트 11 〉	통과 (3.84ms, 10.3MB)
'''