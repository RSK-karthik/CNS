import hashlib

text = "Your text goes here"
# Convert the text to bytes
text_bytes = text.encode('utf-8')

# Create an MD5 hash object
md5_hash = hashlib.md5()

# Update the hash object with the text bytes
md5_hash.update(text_bytes)

# Get the MD5 digest in hexadecimal format
digest = md5_hash.hexdigest()

print("MD5 Digest:", digest)
