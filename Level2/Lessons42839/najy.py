#소수 찾기
import itertools

def isPrime(num):
    if num <= 1: 
        return 0
    
    limit = num**0.5
    for i in range(2, int(limit)+1):
        if num % i == 0:
            return 0
        
    return 1

def solution(numbers):
    answer = 0
    prime = []
    
    numbers = list(numbers)
    
    for i in range(1,len(numbers)+1):
        targets = list(itertools.permutations(numbers,i))

        for target in targets:
            prime.append(int(''.join(target)))
        
    prime = list(set(prime))
    
    for num in prime:
        answer += isPrime(num)
    
    return answer

'''
테스트 1 〉	통과 (0.09ms, 10.4MB)
테스트 2 〉	통과 (4.05ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.5MB)
테스트 4 〉	통과 (1.02ms, 10.4MB)
테스트 5 〉	통과 (7.58ms, 12MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.13ms, 10.3MB)
테스트 8 〉	통과 (12.11ms, 12.1MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
테스트 10 〉	통과 (6.69ms, 10.6MB)
테스트 11 〉	통과 (1.12ms, 10.5MB)
테스트 12 〉	통과 (0.23ms, 10.5MB)
'''