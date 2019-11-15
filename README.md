# Base64 Encoder / Decoder

```python
from encoder.base64 import base64_encode, base64_decode, base64_decode_bytes

# encode string
string = "hello, world"
encoded = base64_encode(string)

# decode string
decoded = base64_decode(encoded)

# encode bytes
data = [1, 2, 3]
encoded = base64_encode(data)

# decode bytes
decoded = base64_decode_bytes(encoded)
```
