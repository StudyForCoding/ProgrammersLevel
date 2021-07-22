# 쿼ㄷ드압축후 개수 세기
def solution(arr):
    h = len(arr) // 2
    if sum([sum(i) for i in arr]) == len(arr) ** 2:
        return [0, 1]
    elif sum([sum(i) for i in arr]) == 0:
        return [1, 0]
    else:
        return [sum(i) for i in zip(*[solution([i[:h] for i in arr[:h]]),
                                      solution([i[h:] for i in arr[:h]]),
                                      solution([i[:h] for i in arr[h:]]),
                                      solution([i[h:] for i in arr[h:]])])]
# 테스트 1 〉	통과 (1.89ms, 10.2MB)
# 테스트 2 〉	통과 (1.33ms, 10.2MB)
# 테스트 3 〉	통과 (0.57ms, 10.3MB)
# 테스트 4 〉	통과 (0.14ms, 10.3MB)
# 테스트 5 〉	통과 (437.67ms, 12.6MB)
# 테스트 6 〉	통과 (135.61ms, 12.7MB)
# 테스트 7 〉	통과 (54.63ms, 12.7MB)
# 테스트 8 〉	통과 (22.09ms, 12.7MB)
# 테스트 9 〉	통과 (8.72ms, 12.7MB)
# 테스트 10 〉	통과 (5.42ms, 18.9MB)
# 테스트 11 〉	통과 (0.09ms, 10.3MB)
# 테스트 12 〉	통과 (0.13ms, 10.4MB)
# 테스트 13 〉	통과 (13.62ms, 12.7MB)
# 테스트 14 〉	통과 (102.20ms, 20.7MB)
# 테스트 15 〉	통과 (158.06ms, 20.7MB)
# 테스트 16 〉	통과 (75.52ms, 12.6MB)