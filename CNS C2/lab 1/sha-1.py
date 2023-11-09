import hashlib

text = "Your text goes here"
# Convert the text to bytes
text_bytes = text.encode('utf-8')

# Create a SHA-1 hash object
sha1_hash = hashlib.sha1()

# Update the hash object with the text bytes
sha1_hash.update(text_bytes)

# Get the SHA-1 digest in hexadecimal format
digest = sha1_hash.hexdigest()

print("SHA-1 Digest:", digest)
