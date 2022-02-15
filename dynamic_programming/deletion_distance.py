def deletion_distance(str1, str2):
  pass # your code goes here

  # 1.  Initialize DP array
  # 2.  Loop through both strings
  # 3.  Base cases for when either index is 0
  # 4.  Two possible outcomes. The last character for both strings either match or they don't
  # 4a. If they match, the delete distance is just what is already calculated for [i - 1][j - 1]
  # 4b. If they don't, we have to delete 1 and add that to the minimum of [i - 1][j] and [i][j - 1]
  #     since we are trying to find the shortest distance 

  str1_length = len(str1)
  str2_length = len(str2)

  # 1.
  result = [[0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)]
  
  # 2.
  for i in range(str1_length + 1):
    for j in range(str2_length + 1):
      # 3.
      if i == 0:
        result[i][j] = j
      # 3.
      elif j == 0:
        result[i][j] = i
      # 4a.
      elif str1[i - 1] == str2[j - 1]:
        result[i][j] = result[i - 1][j - 1]
      # 4b.
      else:
        result[i][j] = 1 + min(result[i - 1][j], result[i][j - 1])
        
  
  print(result)
  return result[str1_length][str2_length]
  
print(deletion_distance('dinitrophenylhydrazine', 'dimethylhydrazine'))

#  '' h e a t
# ''0 1 2 3 4
# h 1 0 1 2 3
# i 2 1 2 3 4
# t 3 2 3 4 3