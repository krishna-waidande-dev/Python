# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
#Ignore punctuation and assume sen will not be empty.

def LongestWord(sen):
  Processed = str.split(sen)
  longest=""
  max=0

  for word in Processed:
    if word.isalpha():
      res=len(word)
      if (res > max):
        max=res
        longest=word
  return longest

print(LongestWord(input()))
