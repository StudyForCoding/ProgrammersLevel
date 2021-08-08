# 2개 이하로 다른 비트
def f(x):
    if x % 2 == 0:
        return x + 1
    else:
        x_bin = "0" + bin(x)[2:]
        x_bin_list = list(x_bin)
        x_bin_0_idx = x_bin.rfind("0")
        x_bin_list[x_bin_0_idx] = "1"
        x_bin_list[x_bin_0_idx+1] = "0"    
        return int("".join(x_bin_list), 2) 

def solution(numbers):
    answer =[]
    for num in numbers:
        answer.append(f(num))
    return answer
'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (1.05ms, 10.3MB)
테스트 2 〉	통과 (59.29ms, 26.2MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.79ms, 10.4MB)
테스트 5 〉	통과 (1.01ms, 10.3MB)
테스트 6 〉	통과 (0.88ms, 10.3MB)
테스트 7 〉	통과 (75.77ms, 26MB)
테스트 8 〉	통과 (72.49ms, 25.2MB)
테스트 9 〉	통과 (70.55ms, 25MB)
테스트 10 〉	통과 (140.98ms, 26.8MB)
테스트 11 〉	통과 (151.04ms, 26.8MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''