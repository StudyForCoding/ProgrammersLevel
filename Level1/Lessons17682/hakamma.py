#17682 다트 게임

def solution(dartResult):
    dart = list(dartResult)
    answer = 0
    score = []
    t = 0
    for i in range(0,len(dart)):
        if dart[i].isdigit():
            if dart[i+1].isdigit():
                score.append(10)
            elif dart[i-1].isdigit():
                continue
            else:
                score.append(int(dart[i]))
        else:
            if dart[i] == 'D':
                score[t]**=2
                t+=1
            elif dart[i] == 'T':
                score[t]**=3
                t+=1
            elif dart[i] == 'S':
                score[t]**=1
                t+=1
                
            elif dart[i] == '#':
                score[t-1]*=(-1)
                
            elif dart[i] == '*':
                if len(score) == 1:
                    score[t-1]*=2
                    
                else:
                    score[t-1]*=2
                    score[t-2]*=2
                
    
    answer = sum(score)
            
    return answer