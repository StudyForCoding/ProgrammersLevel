#가장 큰 수
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))

'''테스트 1 〉	통과 (750.94ms, 23.3MB)
테스트 2 〉	통과 (234.96ms, 17.1MB)
테스트 3 〉	통과 (1271.80ms, 27.4MB)
테스트 4 〉	통과 (1.60ms, 10.5MB)
테스트 5 〉	통과 (596.19ms, 21.9MB)
테스트 6 〉	통과 (455.75ms, 20.3MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.4MB)'''

'''def equalizer(num):
    adder = 0
    if num==0:
        return 0
    if len(str(num)) == 1:
        adder = 0.3
    if len(str(num)) == 2:
        adder = 0.2
    if len(str(num)) == 3:
        adder = 0.1
    if num == 1000:
        return 999.5

    while num<1000:
        num *= 10
    return num+adder

def solution(numbers):
    numbers.sort(key=lambda x: equalizer(x), reverse=True)
    
    return  str(int("".join(map(str, numbers))))'''