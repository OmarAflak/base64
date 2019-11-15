from encoder.base64 import base64_encode

character_set = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=')

def test_base64_encode_characters():
    encoded = base64_encode("omar aflak")
    good = True
    for c in encoded:
        if c not in character_set:
            good = False
    assert good