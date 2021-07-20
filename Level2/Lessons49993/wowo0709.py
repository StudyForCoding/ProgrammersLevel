# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for skillTree in skill_trees:
        idx = 0
        # 파이썬 for-else: break 없이 for문을 돌았을 경우 else 문을 실행
        for i in range(len(skill)):
            newIdx = skillTree.find(skill[i])       # 스킬의 인덱스
            if -1 < newIdx < idx: break             # 있는데 맞지 않을 때
            elif newIdx == -1: idx = len(skillTree) # 없을 때
            else: idx = newIdx                      # 있는데 맞을 때
        else: answer += 1

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''