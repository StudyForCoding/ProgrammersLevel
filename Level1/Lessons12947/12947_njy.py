#하샤드 수
def solution(x):
    #x -> str -> 각 자리 int로 합하기 -> list로 sum -> x를 나눈 나머지로 판단
    return True if x % sum(list(int(str(x)[i]) for i in range (len(str(x))))) == 0 else False
'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
'''