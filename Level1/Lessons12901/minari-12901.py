def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    #월은 1월부터 시작,4월이라면 3월까지만 더해야 하므로 a-1
    day = sum(month[0:a-1]) + b
    
    answer = week[(day%7)-1]
    return answer

#요일의 이름 저장 :SUN,MON,TUE,WED,THU,FRI,SAT
#윤년 : 2/29일까지 -> 1년 = 366일
#1월 1일부터 일수로 계산하고, %7 = week의 ?번째 요소

![image-20210627203121106](C:\Users\mina1\AppData\Roaming\Typora\typora-user-images\image-20210627203121106.png)

![image-20210627203153622](C:\Users\mina1\AppData\Roaming\Typora\typora-user-images\image-20210627203153622.png)

