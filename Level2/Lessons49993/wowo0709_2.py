# 스킬트리

# 역발상: skill 순서대로 skillTree에 있는지 검사하는 것이 아니라,
# skilltree 순서대로 skill에 있는지 검사
def solution(skill, skill_trees):
    answer = 0

    for skillTree in skill_trees:
        skill_list = list(skill)
        for s in skillTree:
            if s in skill and s != skill_list.pop(0): break
        else: answer += 1

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''