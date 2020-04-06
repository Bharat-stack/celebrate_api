import jwt
token=jwt.encode({"id":"sex"}, "dont tell anyone")

print(token)