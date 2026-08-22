# pip install qrcode[pil] matplotlib

import base64, zlib
from matplotlib import pyplot as plt
import qrcode

cipher_b64 = "MdXy+bYrisxUXn8UkUPIXtJdZ6VKWBrJ6xJnJfL5qiuazEReP0owksilz8KEXj9jS0mzmWx8"
key = 73

raw        = base64.b64decode(cipher_b64)
compressed = bytes(b ^ key for b in raw)
message    = zlib.decompress(compressed).decode("utf-8")

img = qrcode.make(message)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()
