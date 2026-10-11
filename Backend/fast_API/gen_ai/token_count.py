import tiktoken

enc = tiktoken.get_encoding("o200k_base")

text = "hello we are from pune"

token = enc.encode(text)

print(f"token content {token}")
print(f"token count {len(token)}")

