#Reverse the order of words in a sentence.
def reverse_words(s):
  words = s.split(' ')
  words.reverse()
  return ' '.join(words)

print(reverse_words("I am a human being"))