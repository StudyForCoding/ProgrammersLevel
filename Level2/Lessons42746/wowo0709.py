# 가장 큰 수

# 초기 코드
def solution(nums):
    if sum(nums) == 0: return '0'
    nums = list(map(str,nums))
    for i in range(len(nums)): nums[i] = [(nums[i]*4)[:4],len(nums[i])]
    nums.sort(key=lambda x:int(x[0]),reverse=True)
    return ''.join(list(map(lambda x:x[0][:x[1]],nums)))

'''
정확성  테스트
테스트 1 〉	통과 (78.34ms, 28.6MB)
테스트 2 〉	통과 (42.64ms, 20.1MB)
테스트 3 〉	통과 (133.51ms, 34.3MB)
테스트 4 〉	통과 (1.86ms, 10.8MB)
테스트 5 〉	통과 (68.14ms, 26.7MB)
테스트 6 〉	통과 (60.71ms, 24.4MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.5MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''

# 좀 더 깔끔한 코드
def solution(nums):
    if sum(nums) == 0: return '0'
    nums = list(map(str,nums))
    nums.sort(key=lambda num:num*3, reverse=True)
    return ''.join(nums) 

'''
정확성  테스트
테스트 1 〉	통과 (43.61ms, 23.3MB)
테스트 2 〉	통과 (24.76ms, 17.1MB)
테스트 3 〉	통과 (57.37ms, 27.5MB)
테스트 4 〉	통과 (1.38ms, 10.5MB)
테스트 5 〉	통과 (38.19ms, 21.9MB)
테스트 6 〉	통과 (33.33ms, 20.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''