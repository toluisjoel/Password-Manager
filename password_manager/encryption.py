import rsa
import base64


class EncryptDecrypt:
    def __init__(self):
        self.publicKey, self.privateKey = rsa.newkeys(512)

    def encrypt(self, password):
        encMessage = rsa.encrypt(password.encode(), self.publicKey)

        return encMessage

    def decrypt(self, password):
        # encMessage = rsa.encrypt(password.encode(), self.publicKey)
        encMessage = base64.b64decode(password).decode("ASCII")
        decMessage = rsa.decrypt(encMessage, self.privateKey).decode()

        return encMessage


# a = EncryptDecrypt()
# print(a.encrypt('tolu'))
# print(a.decrypt())


#!/usr/bin/env python3

# from Crypto.PublicKey import RSA
# from Crypto import Random
# import base64

# key_pair = RSA.generate(1024, Random.new().read(1024 // 8))
# public_key = key_pair.publickey()

# secret = "123456"

# enc_secret = public_key.encrypt(secret.encode("utf-8"), 32)[0]
# enc_secret_b64 = base64.b64encode(enc_secret)
# print(enc_secret_b64)

# enc_secret = base64.b64decode(enc_secret_b64)
# secret = key_pair.decrypt(enc_secret)
# print(secret.decode("utf-8"))
# 123456