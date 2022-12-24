from cryptography import crypto
key = input("enter the session key")
with open("hash.sidecan", "w") as f:
    f.write(key)  
for x in range(850):
    crypto()
