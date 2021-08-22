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
            prime.append(int(''.join(map(str,target))))
        
    prime = list(set(prime))
    
    for num in prime:
        answer += isPrime(num)
    
    return answer