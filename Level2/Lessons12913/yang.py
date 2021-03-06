# 땅따먹기
def solution(land):
    import copy
    copy_land = copy.deepcopy(land)
    for idx in range(len(land)-1):
        land[idx+1][0] += max(land[idx][1], land[idx][2], land[idx][3])
        land[idx+1][1] += max(land[idx][0], land[idx][2], land[idx][3])
        land[idx+1][2] += max(land[idx][0], land[idx][1], land[idx][3])
        land[idx+1][3] += max(land[idx][0], land[idx][1], land[idx][2])
    
    for i in range(len(land) - 2,-1,-1):
        copy_land[i][0] += max(copy_land[i+1][1], copy_land[i+1][2], copy_land[i+1][3])
        copy_land[i][1] += max(copy_land[i+1][0], copy_land[i+1][2], copy_land[i+1][3])
        copy_land[i][2] += max(copy_land[i+1][0], copy_land[i+1][1], copy_land[i+1][3])
        copy_land[i][3] += max(copy_land[i+1][0], copy_land[i+1][1], copy_land[i+1][2])
    answer1 = max(land[-1][0], land[-1][1], land[-1][2], land[-1][3])
    answer2 = max(copy_land[0][0], copy_land[0][1], copy_land[0][2], copy_land[0][3])
    return max(answer1,answer2)
# 테스트 1 〉	통과 (7.03ms, 10.6MB)
# 테스트 2 〉	통과 (6.95ms, 10.6MB)
# 테스트 3 〉	통과 (6.56ms, 10.7MB)
# 테스트 4 〉	통과 (7.06ms, 10.6MB)
# 테스트 5 〉	통과 (6.97ms, 10.6MB)
# 테스트 6 〉	통과 (6.55ms, 10.6MB)
# 테스트 7 〉	통과 (7.07ms, 10.6MB)
# 테스트 8 〉	통과 (6.93ms, 10.6MB)
# 테스트 9 〉	통과 (7.00ms, 10.7MB)
# 테스트 10 〉	통과 (7.03ms, 10.7MB)
# 테스트 11 〉	통과 (6.71ms, 10.6MB)
# 테스트 12 〉	통과 (6.42ms, 10.7MB)
# 테스트 13 〉	통과 (7.06ms, 10.5MB)
# 테스트 14 〉	통과 (7.10ms, 10.6MB)
# 테스트 15 〉	통과 (6.55ms, 10.6MB)
# 테스트 16 〉	통과 (8.19ms, 10.6MB)
# 테스트 17 〉	통과 (7.27ms, 10.6MB)
# 테스트 18 〉	통과 (7.03ms, 10.6MB)
# 효율성  테스트
# 테스트 1 〉	통과 (544.39ms, 57MB)
# 테스트 2 〉	통과 (544.72ms, 56.9MB)
# 테스트 3 〉	통과 (567.50ms, 57.1MB)
# 테스트 4 〉	통과 (538.74ms, 57MB)