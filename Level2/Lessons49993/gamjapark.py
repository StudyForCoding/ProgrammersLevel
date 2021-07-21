# 스킬트리

import re
def solution(skill, skill_trees):
    answer = len(skill_trees)
    sep = "|".join(list(skill))
    for skill_tree in skill_trees:
        skills = re.findall(sep,skill_tree)
        for i in range(len(skills)):
            if skills[i] != skill[i]:
                answer -= 1
                break
    return answer

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.11ms, 10.2MB)
테스트 2 〉	통과 (0.11ms, 10.3MB)
테스트 3 〉	통과 (0.13ms, 10.1MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (1.19ms, 10.2MB)
테스트 6 〉	통과 (0.12ms, 10.1MB)
테스트 7 〉	통과 (0.13ms, 10.2MB)
테스트 8 〉	통과 (0.14ms, 10.2MB)
테스트 9 〉	통과 (0.15ms, 10.1MB)
테스트 10 〉	통과 (0.13ms, 10.1MB)
테스트 11 〉	통과 (0.15ms, 10.2MB)
테스트 12 〉	통과 (0.27ms, 10.2MB)
테스트 13 〉	통과 (0.14ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''