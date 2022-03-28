def flatten_dictionary(dictionary):
  output = {}
  
  def dfs(prev_key, next_dictionary):    
    for key in next_dictionary: # next_dictionary = {'x': 1}
      if key == "":
        new_key = prev_key
      else:
        if prev_key == "":
            new_key = key
        else:
            new_key = prev_key + "." + key   

      if isinstance(next_dictionary, dict):
        dfs(new_key, next_dictionary[key])
      else:
        output[prev_key] = next_dictionary #key2.c, we are 'd' -> key2.c.d
  
  for key in input:
      dfs(key, dictionary[key])
    
  return output
""

"""
dfs(prev_key, next_dictionary):
for key in next_dictonary:


dictionar[key2][a] -> 2

dict[key2] -> another dict

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
        
Approach:

Base case. Value is flat. If not flat, travel until flat.
Append subkey name to main key. With recursion

Time  : O(n)
Space : O(1)


feedback:

Good: 
1. think out loud
2. 

Bad
1. python sytanx
2. more practice on recursion, backtracking
3. 

"""

input = {"Key":{"a":"2","b":"3"}}

print(flatten_dictionary(input))