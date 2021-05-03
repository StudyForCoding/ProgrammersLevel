def solution(answers):
    import copy
    import numpy as np
    answer = []
    answers = np.append(answers,np.zeros(40 - len(answers)%40))
    label1 = np.array([1, 2, 3, 4, 5])
    label2 = np.array([2, 1, 2, 3, 2, 4, 2, 5])
    label3 = np.array([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    cor1 = np.array([])
    cor2 = np.array([])
    cor3 = np.array([])
    for x in range(len(answers)//5):
        cor1 = np.append(cor1,answers[x*5: x*5 + 5] - label1)
    for x in range(len(answers)//8):
        cor2 = np.append(cor2,answers[x*8: x*8 + 8] - label2)
    for x in range(len(answers)//10):
        cor3 = np.append(cor3,answers[x*10: x*10 + 10] - label3)
    point1 = np.sum(np.where(cor1 == 0, 1, 0))
    point2 = np.sum(np.where(cor2 == 0, 1, 0))
    point3 = np.sum(np.where(cor3 == 0, 1, 0))
    point_dict = {1:point1, 2:point2, 3:point3}
    top = max(point_dict.values())
    answer = [idx for idx, score in point_dict.items() if score == top]
    #point = np.array([point1, point2, point3])
    #answer = np.argmax([point1,point2,point3])
    # x = np.max(point)
    # answer = np.where(point == x)[0]
    # answer = list(np.where(point == x)[0])
    
    return answer