# [1차] 비밀지도

def solution(n, arr1, arr2):
    map = []
    for i in range(n): # 십진수 두 개를 or 비트연산 후 길이에 맞게 앞에 0을 채우고 특정 문자 대체
        map.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace("1","#").replace("0"," "))
    return map

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
'''
