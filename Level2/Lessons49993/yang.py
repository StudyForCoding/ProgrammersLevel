# 스킬트리
def solution(skill, skill_trees):
    answer = 0
    # a = [11,10,12,13,20,31,11,10,10,11]
    # print(a.index(9))
    
    for tree in skill_trees:
        tmp_skill = list(skill)
        for sk in tree:
            if sk in skill:
                if len(tmp_skill) == 0:
                    print(tree)
                    print(answer)
                    print('error')
                    answer -= 1
                    break
                elif sk == tmp_skill[0]:
                    tmp_skill.pop(0)
                else:
                    print(tree)
                    print(answer)
                    print('else')
                    answer -= 1
                    break
        print(tree)
        print(answer)
        print('plus')
        answer += 1
    return answer
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.04ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.2MB)
# 테스트 13 〉	통과 (0.05ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10MB)