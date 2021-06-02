# 소수 만들기
import math 
import itertools
def is_prime_number(x,answer):
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return answer
  answer += 1
  return answer
def solution(nums):
  answer = 0
  result = list(itertools.combinations(nums,3))
  for (i,j,k) in result:
    answer = is_prime_number(i+j+k, answer)
  return answer

# 테스트 1 〉	통과 (2.31ms, 10.1MB)
# 테스트 2 〉	통과 (3.18ms, 10.4MB)
# 테스트 3 〉	통과 (0.91ms, 10.3MB)
# 테스트 4 〉	통과 (0.76ms, 10.2MB)
# 테스트 5 〉	통과 (3.35ms, 10.4MB)
# 테스트 6 〉	통과 (5.44ms, 10.2MB)
# 테스트 7 〉	통과 (0.28ms, 10.1MB)
# 테스트 8 〉	통과 (12.94ms, 11.2MB)
# 테스트 9 〉	통과 (1.21ms, 10.3MB)
# 테스트 10 〉	통과 (10.48ms, 10.7MB)
# 테스트 11 〉	통과 (0.13ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.2MB)
# 테스트 13 〉	통과 (0.17ms, 10.2MB)
# 테스트 14 〉	통과 (0.07ms, 10.3MB)
# 테스트 15 〉	통과 (0.07ms, 10.1MB)
# 테스트 16 〉	통과 (12.73ms, 11.1MB)
# 테스트 17 〉	통과 (12.24ms, 11.3MB)
# 테스트 18 〉	통과 (0.14ms, 10.1MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (16.97ms, 11.4MB)
# 테스트 21 〉	통과 (16.41ms, 11.4MB)
# 테스트 22 〉	통과 (2.58ms, 10.3MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (13.35ms, 11.1MB)
# 테스트 25 〉	통과 (13.20ms, 11.1MB)
# 테스트 26 〉	통과 (0.01ms, 10.2MB)