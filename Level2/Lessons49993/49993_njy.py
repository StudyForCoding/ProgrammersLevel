# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = []
        for skill_current in skill_tree:
            if skill_current in skill:
                skill_list.append(skill_current)
        flag = True
        for idx in range(len(skill_list)):
            if skill_list[idx] != skill[idx]:
                flag = False
                break
        if flag:
            answer += 1
                
    return answer

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
"""