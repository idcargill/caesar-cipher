import pytest
from caesar_cipher import encrypt, decrypt

@pytest.mark.parametrize(
  'input,shift, expected', 
  [
    ('a', 0, 'a'),
    ('a', 1, 'b'),
    ('a', 2, 'c'),
    ('a', 3, 'd'),
    ('a', 4, 'e'),
    ('a', 5, 'f'),
    ('aaa', 2, 'ccc'),
    ('zzz', -1, 'yyy'),
    ('zzz', -2, 'xxx'),
    ('a', -1, 'z'),
    ('a', -2, 'y'),
    ('a', -3, 'x'),
    ('z', 1, 'a'),
    ('z', 2, 'b'),
    ('zzz', 6, 'fff'),
    ('cat', 3, 'fdw'),
    ('abc', 10, 'klm'),
    ('abc', 27, 'bcd')
  ]
)
def test_encrypt(input, shift, expected):
  assert encrypt(input,shift) == expected


@pytest.mark.parametrize(
  'input, shift, expected', 
  [
    ('klm', 10, 'abc'),
    ('fdw', 3, 'cat'),
    ('a', 1, 'z')
  ]
)
def test_decrypt(input, shift, expected):
  assert decrypt(input, shift) == expected
