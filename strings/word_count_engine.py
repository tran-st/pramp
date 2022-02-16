def word_count_engine(document):
  pass # your code goes here

# document = "Practice makes perfect. you'll only
#                   get Perfect by practice. just practice!"

  # 1. Parse through the document character by character
  # 1a. If character is alpha, add it to current_word
  # 1b. If character is a whitespace, add word to dictionary
  # 1c. If character is punctuation, 
  # 2. Checking for white spaces to seperate words
  # 3. Store words in dictionary
  # 4. Remove punctuations 
  # 5. Return dictionary as array, with most occuring word on top
  # 6. Edge cases
  
  word_dictionary = {}
  current_word = ''
  largest_count = 0
  
  for char in document:
    if char.isalpha():
      current_word += char
    elif char == ' ' or char == document[-1]:
      current_word = current_word.lower()
      current_word_count = 0
      
      if current_word in word_dictionary:
        current_word_count = word_dictionary[current_word]
        current_word_count += 1
      else:
        current_word_count = 1
      
      word_dictionary[current_word] = current_word_count
      largest_count = max(largest_count, current_word_count)
        
      current_word = ''
      
      
  count_list = [None] * (largest_count + 1)
  
  for word, count in word_dictionary.items():
    word_counter_list = count_list[count]
    
    if(word_counter_list is None):
      word_counter_list = []
      
    word_counter_list.append(word)
    count_list[count] = word_counter_list
      
  print(word_dictionary)
  print(largest_count)
  print(word_counter_list)
  print(count_list)
      
  # Can't hear you anymore
  # Lost you
      
  # you'll
  # Expecting youll
  # Actual you
  # ll
  
  # Hey can you put me your email here??

  # What for?
  # I'd be happy to solve other questions
  # together 
  # Sure man, sound good. Also, Pramp gives us that option at the end
  # Anyway, my email is steventran9102@gmail.com
  # Thank you I'll email you. I'm sorry the internet is so bad in here. 
  # No worries, are we ending the session then?
  # I don't mind waiting until you reconnect
  # I may need to go to home. Which will take me around 30 mns so, may be in the coming days when get free time
  # Ok, don't end the session then. I can wait for 30 minutes lol. If you want
  
  # Oh yea definitely. I won't close it
  # Big sorry!
  
  # No worries my friend. It happens. I am in Vietnam, so I also know the struggle of a good 
  
#  internet connection haha
# Ohh good to know. here is unbearable. I'll be here in few mins
  
# Okay.  
# Hey, you back? It's showing you as online
  
  
document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

word_count_engine(document)