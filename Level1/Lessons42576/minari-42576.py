```python
#마라톤에 참여한 선수 : participant , 완주한 선수 : completion
#한 명만! 완주를 하지 못했더 한명만!
#1.participant 정렬하고 completion 정렬하고 두개가 같다면 빼면 안돼?
#2.return : 완주x 선수이름 ( participant - completion )
def solution(participant,completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)): #range(len(completion))으로 하면 'IndexError:list inedex out of range'가 떠. 아마 completion 갯수가 하나 적어서, completion을 다 못돌리니까 그렇지 않을까?
        if participant[i]!=completion[i]:
            return participant[i] #만약에 정렬한 리스트 중간에 다른 이름이 있다면, 그 사람이 완주하지 못한 사람이니까 participant[i] 출력하는거야
    return participant[i+1] #만약 정렬한 리스트 끝에 다른 이름이 있다면 range(len(completion))만큼 for문을 돌려도 if문에 들어가지 않을테니, 그 때엔 participant[i+1]값을 출력하는거야
participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]
```