def solution(n, lost, reserve):
    answer = n
    losts = lost.copy()
    #1.reserve 학생이 lost에도 있을 수 있다. -> 자기가 입을 옷밖에 남지 않았으므로, lost와 reserve에 지워야한다.
    for i in losts:      
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    
    #2. reserve가 lost의 앞뒤번호가 다 포함될 때 중복으로 빌려주면 안되므로, lost 요소 하나를 해결했다면 지워야할듯?
    for j in lost:      
        if j-1 in reserve:
            reserve.remove(j-1)
        elif j+1 in reserve:
            reserve.remove(j+1)
        else:
            answer-=1   #3. answer에 n을 저장해놓고, reserve에서 lost가 빌리지 못했다면 answer-1
    return answer 


#n = 전체 학생 수 , lost = 도난당한 학생들 리스트, reserve = 여벌의 체육복을 가져온 학생들 리스트
#return = 체육수업을 들을 수 있는 학생의 최댓값

![image-20210628154859766](C:\Users\mina1\AppData\Roaming\Typora\typora-user-images\image-20210628154859766.png)

![image-20210628154907811](C:\Users\mina1\AppData\Roaming\Typora\typora-user-images\image-20210628154907811.png)