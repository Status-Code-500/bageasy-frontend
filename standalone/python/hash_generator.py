from cryptography import crypto
key = input("enter the session key")
with open("cryptography\\hash.sidecan", "w") as f:
    f.write(key)
crypto()
