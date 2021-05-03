def solution(a, b):
  label = ['MON','TUE','WED','THU','FRI','SAT','SUN']
  import datetime
  answer = label[datetime.date(2016,a,b).weekday()]
  return answer
print(solution(1, 2))