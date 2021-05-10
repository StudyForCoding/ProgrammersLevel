# 키패드 누르기

from math import *
def find_near(left, right, target, hand, answer):
  left_len = abs((left[0] - target[0]))  + abs((left[1] - target[1])) 
  right_len = abs((right[0] - target[0])) + abs((right[1] - target[1])) 

  if target[1] == 0:
    left = target
    answer += 'L'
    return left, right, answer # left
  elif target[1] == 2:
    right = target
    answer += 'R'
    return left, right, answer # right
  elif left_len < right_len:
    left = target 
    answer += 'L'
    return left, right, answer # left
  elif left_len > right_len:
    right = target
    answer += 'R'
    return left, right, answer # right
  elif hand == 'left':
    left = target
    answer += 'L'
    return left, right, answer # left
  else:
    right = target
    answer += 'R'
    return left, right, answer # right

    
def solution(numbers, hand):
  answer = ''

  keypad = {'1':[0,0], '2':[0,1], '3':[0,2], '4':[1,0], '5':[1,1], '6':[1,2], '7':[2,0], '8':[2,1], '9':[2,2], '*':[3,0], '0':[3,1], '#':[3,2]}
  left = keypad['*']
  right = keypad['#']
  result = None
  for number in numbers:
    left, right, answer = find_near(left, right, keypad[str(number)], hand, answer)
    
  return answer
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.07ms, 10.4MB)
# 테스트 12 〉	통과 (0.07ms, 10.3MB)
# 테스트 13 〉	통과 (0.12ms, 10.3MB)
# 테스트 14 〉	통과 (0.27ms, 10.4MB)
# 테스트 15 〉	통과 (0.71ms, 10.3MB)
# 테스트 16 〉	통과 (0.69ms, 10.2MB)
# 테스트 17 〉	통과 (1.25ms, 10.3MB)
# 테스트 18 〉	통과 (1.29ms, 10.2MB)
# 테스트 19 〉	통과 (1.29ms, 10.2MB)
# 테스트 20 〉	통과 (1.15ms, 10.4MB)