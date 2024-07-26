#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/5/31 14:39
# @File     : gen_seckey_python_demo.py
# @Desc     :
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


def decode_bs64():
    import base64

    # Base64-encoded string
    encoded_data = "SGVsbG8gV29ybGQhCg=="  # Example Base64-encoded string
    encoded_data = "P678%2FfO7GPWmD%2FwpeYdAePFQNoMhC031pTbUsuXSEGpbPZSYvNhvYEdVY2VfDP0quPOH%2BbXZr2Kp%0AuMXd6s38xyrasInrP2EQaoOyp7LRoJRNbpBNg4AoMzQQ70Hfv1YAMkrqOqx4KOOQp0tcienXQf7s%0AcgB26zKfry5wqOWVW5tjGtstaNlIMfejJUGfpo%2FBlqXzLDIYMFT%2BhWCdZZ7L%2FsQA7QySw%2BOzAtgm%0AwfsQE5nRS8QDkiZPYc4eWDz1Rp2909Rtrcg%2B243ZPrj9mIQS%2FKCayyF6E4Oko%2FlBNfmQSai7sQva%0A4FJMFbj3OnYyEYrYyEJhffgQPbSWs2GsMMfsi0lrTB%2FqyM%2F97o8DznRKRp4W1664wAoeuotkqKvE%0Alj3FWv%2F2mdnLrliLBk343rsrn%2F%2BNkU2Sett0gAWV8r0Fpu9E88l8RU7PX7AR3Dg5%2B5%2BBBvDOmB%2FA%0ARTKxbinjVuLGMwYa5v1%2BJNBj91pPjoYStxwGs%2B3E%2BcIhm4fWYMdRQC8xo62DT0F1wkXjm2zgasZy%0AlMWrIb3iUCOhfq0H81dqQQLWP%2FkAbQpOVY%2FGhfhGIfrBImY76JET6TwbkKr9Dw18sVdWCz8KKNJe%0AmcXj%2F%2BXfdSGAJDmvq%2BZKRe8p6S4XQw4kBvXUOG3zu6%2FRgnfPektpVxfpFRsPzO2AH3dUIQv9jVs%3D%0A"
    print(len(encoded_data), len(encoded_data) / 4)
    # Decode Base64-encoded data
    decoded_data = base64.b64decode(encoded_data)

    # Convert bytes to string (if necessary)
    decoded_string = decoded_data.decode('utf-8')

    print(decoded_string)


decode_bs64()


# 生成 DESede 密钥
des_key = DES3.adjust_key_parity(get_random_bytes(24))
des_cipher = DES3.new(des_key, DES3.MODE_ECB)

# 生成 RSA 密钥对
rsa_key = RSA.generate(2048)
rsa_public_key = rsa_key.publickey()

# 使用 RSA 公钥加密
rsa_cipher = PKCS1_OAEP.new(rsa_public_key)
encrypted_data = rsa_cipher.encrypt(b'Some data to encrypt')

# 打印加密结果
print(encrypted_data)
