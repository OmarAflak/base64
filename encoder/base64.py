def base64_code_to_char(n):
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

def base64_char_to_code(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 26
    elif '0' <= c <= '9':
        return ord(c) - ord('0') + 52
    elif c == '+':
        return 62
    elif c == '/':
        return 63
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
    trailing_zeros = 3 - size % 3 if size % 3 > 0 else 0
    stream += '000000' * trailing_zeros
    new_stream = [stream[i:i+6] for i in range(0, len(stream), 6)]
    new_data = [int(binary, 2) for binary in new_stream]
    new_chars = [base64_code_to_char(n) for n in new_data[:len(new_data) - trailing_zeros]]
    new_chars.extend(['='] * trailing_zeros)
    return ''.join(new_chars)

def base64_decode(string):
    data = base64_decode_bytes(string)
    return ''.join([chr(n) for n in data])

def base64_decode_bytes(string):
    padding = sum([1 for c in string[-2:] if c == '='])
    data = [base64_char_to_code(c) for c in string[:len(string) - padding]]
    stream = ''.join(['{0:06b}'.format(n) for n in data])
    return [int(stream[i:i + 8], 2) for i in range(0, len(stream), 8)]
