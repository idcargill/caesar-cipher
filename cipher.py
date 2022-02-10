import string
from nltk.corpus import words

# # nltk.download()
word_list = words.words()

all_letters = string.ascii_lowercase + string.ascii_uppercase

low = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
full_alphabet_list = list(all_letters)

lower_case = dict(zip(low, range(26)))
upper_case = dict(zip(upper, range(26)))


def encrypt(word, shift):
  encrypted_text = ''
  for i in word:
    if i not in full_alphabet_list:
      encrypted_text += i 
      continue

    if i in lower_case:
      num = lower_case[i] + shift
      if num > 25:
        num = num % 26
      encrypted_text += low[num]
    elif i in upper_case:
      num = upper_case[i] + shift
      if num > 25:
        num = num % 26
      encrypted_text += upper[num]
  return encrypted_text

def decrypt(word, shift):
  decrypted = encrypt(word, -shift)
  return decrypted

def crack(secret):
  shifted = 0
  found_words = 0
  encrypted_words = secret.split()
  final = ''
  
  while shifted < 25 and found_words < len(encrypted_words) * 0.7:
    decrypted = decrypt(secret, shifted)
    shifted += 1
    for word in decrypted.split():
      if word in word_list:
        print(word)
        found_words += 1
    
  if found_words > len(encrypted_words) * 0.9:
    print(found_words)
    final = decrypted
  else:
    final = ''
  
  return final


