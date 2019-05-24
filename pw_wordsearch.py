#primaditaningtyas.w@gmail.com
#ref : https://zhaqenl.github.io/en/wordsearch/

import sys

path = sys.argv[1]
  
def matrixify(string_grid, separator='\n'):
  return string_grid.split(separator)
def coord_char(coord,matrix):
  row_index,column_index=coord
  return matrix[row_index][column_index]
def convert_to_word(coord_matrix,matrix):
  return ''.join([coord_char(coord,matrix) for coord in coord_matrix])
def find_base_match(char,matrix):
  base_matches = []
  for row_index, row in enumerate(matrix):
    for column_index, column in enumerate(row):
      if char == column:
        base_matches.append((row_index, column_index))
  return base_matches
def matched_neighbors(coord,second_char,matrix,row_length,column_length):
  row_number,column_number = coord
  neighbors_coordinates = [(row,column) 
                          for row in range(row_number-1,row_number+2)
                          for column in range(column_number-1,column_number+2)
                          if row_length > row >= 0
                          and column_length > column >= 0
                          and coord_char((row,column),matrix) == second_char
                          and not (row,column) == coord]
  return neighbors_coordinates
def complete_line(base_coord,targ_coord,word_len,row_length,column_length):
  if word_len == 2:
    return base_coord, targ_coord

  line = [base_coord,targ_coord]
  diff_1,diff_2 = targ_coord[0]-base_coord[0],targ_coord[1]-base_coord[1]

  for _ in range(word_len-2):
    line += [(line[-1][0] + diff_1, line[-1][1] + diff_2)]
  
  if 0 <= line[-1][0] <= row_length-1 and 0 <= line[-1][1] <= column_length-1:
    return line

  return []
def complete_match(word,matrix,base_matches,word_len,row_length,column_length):
  match_candidates = (complete_line(base,neighbor,word_len,row_length,column_length)
                      for base in base_matches
                      for neighbor in matched_neighbors(base,word[1],matrix,row_length,column_length))

  return [match for match in match_candidates if convert_to_word(match, matrix) == word]
def find_matches(word, string_grid, separator='\n'):
  word_len = len(word)
  if isinstance(string_grid, list):
    matrix = string_grid
  else:
    matrix = matrixify(string_grid, separator)

  row_length, column_length = len(matrix), len(matrix[0])
  base_matches = find_base_match(word[0], matrix)

  if column_length < word_len > row_length or not base_matches:
    return []
  elif word_len == 1:
    return base_matches

  return complete_match(word, matrix, base_matches, word_len, row_length, column_length)
def wordsearch(word, string_grid, separator='\n'):
  return len(find_matches(word, string_grid, separator))

with open(path) as f:
  lst = f.read().split()
  
  u=1
  v=2
  
  
  for case in range(1,int(lst[0])+1):
    h = int(lst[u])
    #w = int(lst[v])
    #grid_height = h
    #grid_width = w
    f_let_pos = u+2
    l_let_pos = u+h+1
    word_pos = u+h+2
    
    lst_grid = lst[f_let_pos:l_let_pos+1]
    
    grid = " ".join(lst_grid)    
    word = lst[word_pos]
        
    print("Case ",case,": ",wordsearch(word,grid," "),sep="")
    
    u = h+u+3
    v = h+v+3