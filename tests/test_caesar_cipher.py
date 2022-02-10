import pytest
from cipher import encrypt, decrypt

@pytest.mark.parametrize(
  'input,shift, expected', 
  [
    ('a', 0, 'a'),
    ('a', 5, 'f'),
    ('aaa', 2, 'ccc'),
    ('z!z', -1, 'y!y'),
    (' a?', -1, ' z?'),
    ('a', -3, 'x'),
    ('z', 2, 'b'),
    ('cat', 3, 'fdw'),
    ('ab 7 c', 10, 'kl 7 m'),
    ('AaA', 2, 'CcC' ),
    ('aAa?  bBb!', 2, 'cCc?  dDd!')
  ]
)
def test_encrypt(input, shift, expected):
  assert encrypt(input,shift) == expected


def test_decrypt():
  phrase = 'cat'
  secret = encrypt(phrase, 5)
  assert phrase == decrypt(secret, 5)



def test_decrypt_10():
  phrase = 'It was the best of times, it was the worst of times.'
  secret = encrypt(phrase, 10)
  assert phrase == decrypt(secret, 10)
