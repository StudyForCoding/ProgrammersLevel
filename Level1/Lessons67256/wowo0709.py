# [카카오 인턴] 키패드 누르기

def manhattanDist(pos1,pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def solution(numbers, hand):
    answer = ''
    l,r = 10,12 # 10 = *, 12 = #
    pos = {0:[3,1]} # 키패드 숫자의 위치(행,열)
    for n in range(1,13): 
        pos[n] = [(n-1)//3,(n-1)%3] # 행,열
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            l = numbers[i]
            answer += 'L'
        elif numbers[i] in [3,6,9]:
            r = numbers[i]
            answer += 'R'
        else:
            l_d = manhattanDist(pos[l],pos[numbers[i]])
            r_d = manhattanDist(pos[r],pos[numbers[i]])
            if l_d > r_d:
                r = numbers[i]
                answer += 'R'
            elif l_d < r_d:
                l = numbers[i]
                answer += 'L'
            else: # l_d == r_d
                if hand == 'left':
                    l = numbers[i]
                    answer += 'L'
                else: # hand == 'right'
                    r = numbers[i]
                    answer += 'R'
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉통과 (0.02ms, 10.4MB)
테스트 11 〉통과 (0.05ms, 10.2MB)
테스트 12 〉통과 (0.03ms, 10.2MB)
테스트 13 〉통과 (0.06ms, 10.3MB)
테스트 14 〉통과 (0.16ms, 10.2MB)
테스트 15 〉통과 (0.36ms, 10.3MB)
테스트 16 〉통과 (0.35ms, 10.3MB)
테스트 17 〉통과 (0.73ms, 10.2MB)
테스트 18 〉통과 (0.78ms, 10.3MB)
테스트 19 〉통과 (0.77ms, 10.3MB)
테스트 20 〉통과 (0.83ms, 10.3MB)
'''