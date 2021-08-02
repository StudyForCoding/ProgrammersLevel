# 2개 이하로 다른 비트
def cal(numbers):
    numbers = '000000' + bin(numbers)[2:] 
    answer = []
    if numbers[-1] == '0':
        
        return int(numbers[:-1] + '1',2)
    numbers = numbers[::-1]
    for idx, ch in enumerate(numbers):
        if ch == '1':
            pass
        elif ch == '0':
            numbers = numbers[:idx-1] + '01'+numbers[idx+1:]
            break
    numbers = numbers[::-1]
    return int(numbers, 2)
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(cal(number))
    return answer
# 테스트 1 〉	통과 (1.35ms, 10.3MB)
# 테스트 2 〉	통과 (88.99ms, 26.1MB)
# 테스트 3 〉	통과 (0.16ms, 10.2MB)
# 테스트 4 〉	통과 (1.35ms, 10.3MB)
# 테스트 5 〉	통과 (1.45ms, 10.4MB)
# 테스트 6 〉	통과 (1.26ms, 10.3MB)
# 테스트 7 〉	통과 (104.56ms, 25.3MB)
# 테스트 8 〉	통과 (96.19ms, 24.8MB)
# 테스트 9 〉	통과 (89.75ms, 24.1MB)
# 테스트 10 〉	통과 (264.11ms, 26.8MB)
# 테스트 11 〉	통과 (262.71ms, 26.8MB)