import string
# import nltk
from nltk.corpus import words
# # nltk.download()

word_list = words.words()
print(len(word_list))
# Letter / index keys
alphabet_string = string.ascii_lowercase
a_list = list(alphabet_string)
number_key = dict(zip(a_list, range(26)))

def encrypt(word, shift):
  encrypted_text = ''
  for i in word:
    num = number_key[i] + shift
    if num > 25:
      num = num % 26
    encrypted_text += a_list[num]
  return encrypted_text

def decrypt(word, shift):
  return encrypt(word, -shift)


def crack(word):
  pass

print(word_list)