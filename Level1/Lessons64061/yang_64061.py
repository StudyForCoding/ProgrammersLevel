import numpy as np
def pick(board,y):
  for x,value in enumerate(board[y-1]):
    if value != 0:
      board[y-1,x] = 0
      return [y-1,x], value
  return [],-1
def solution(board, moves):

  answer = 0
  label = [-10]
  board = np.transpose(board)
  for number in moves:
    tmp_idx, tmp_value = pick(board,number)
    if tmp_value != -1:
      if label[-1] == tmp_value:
        label = label[:-1]
        answer += 2
      else:
        label.append(tmp_value)
  return answer