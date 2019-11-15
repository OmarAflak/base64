import random
import string

from encoder.base64 import base64_encode

character_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=')

def random_string(stringLength=100):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def test_characters():
    string = random_string()
    encoded = base64_encode(string)
    good = True
    for c in encoded:
        if c not in character_set:
            good = False
    assert good

def test_ending_equal():
    string = random_string()
    encoded = base64_encode(string)
    substr = encoded[:-2]
    assert '=' not in substr

def test_simple():
    assert base64_encode("omar aflak") == "b21hciBhZmxhawo="

def test_length():
    string = random_string()
    assert len(base64_encode(string)) > len(string)