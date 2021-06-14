#소수 찾기
def solution(n):
    numbers = set()
    for i in range(3,n+1):
        numbers.add(i)
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                numbers.remove(i)
                break
    return len(numbers)+1
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.20ms, 10.3MB)
테스트 3 〉	통과 (0.49ms, 10.3MB)
테스트 4 〉	통과 (1.09ms, 10.3MB)
테스트 5 〉	통과 (0.71ms, 10.2MB)
테스트 6 〉	통과 (7.41ms, 10.3MB)
테스트 7 〉	통과 (2.43ms, 10.3MB)
테스트 8 〉	통과 (5.65ms, 10.4MB)
테스트 9 〉	통과 (9.40ms, 10.4MB)
테스트 10 〉	통과 (619.32ms, 16MB)
테스트 11 〉	통과 (2880.44ms, 20.5MB)
테스트 12 〉	통과 (695.66ms, 15.9MB)
효율성  테스트
테스트 1 〉	통과 (3188.80ms, 20.4MB)
테스트 2 〉	통과 (3054.48ms, 20.3MB)
테스트 3 〉	통과 (3168.82ms, 20.3MB)
테스트 4 〉	통과 (3122.13ms, 20.3MB)
'''