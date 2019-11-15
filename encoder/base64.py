def base64_encode(data):
    if type(data) is str:
        return base64_encode_string(data)
    elif type(data) is list:
        return base64_encode_bytes(data)
    return None

def base64_encode_string(string):
    data = [ord(c) for c in string]
    return base64_encode_bytes(data)

def base64_encode_bytes(data):
    stream = ''.join(['{0:08b}'.format(n) for n in data])
    return base64_encode_binary(stream)

def base64_encode_binary(stream):
    pass