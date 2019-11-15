def base64_char_mapping(n):
    if 0 <= n <= 25:
        return chr(n + ord('A'))
    elif 26 <= n <= 51:
        return chr(n + ord('a') - 26)
    elif 52 <= n <= 61:
        return chr(n + ord('0') - 52)
    elif n == 62:
        return '+'
    elif n == 63:
        return '/'
    return None

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
    size = len(stream) // 8
    trailing_zeros = 3 - size % 3
    stream += '000000' * trailing_zeros
    new_stream = [stream[i:i+6] for i in range(0, len(stream), 6)]
    new_data = [int(binary, 2) for binary in new_stream]
    new_chars = [base64_char_mapping(n) for n in new_data[:-trailing_zeros]]
    new_chars.extend(['='] * trailing_zeros)
    return ''.join(new_chars)