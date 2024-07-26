from Crypto.Cipher import DES3


# 这里给出一个使用Python语言实现3DES加密算法的例程，需要使用pycryptodome库进行支持。代码如下：
def des3_encrypt(key, plaintext):
    key = key.encode('utf-8')
    plaintext = plaintext.encode('utf-8')

    # 填充明文
    length = 8 - (len(plaintext) % 8)
    plaintext += bytes([length]) * length

    # 初始化加密器
    cipher = DES3.new(key, DES3.MODE_CBC, b'\0' * 8)

    # 加密
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext


def des3_decrypt(key, ciphertext):
    key = key.encode('utf-8')

    # 初始化解密器
    cipher = DES3.new(key, DES3.MODE_CBC, b'\0' * 8)

    # 解密
    plaintext = cipher.decrypt(ciphertext)

    # 去除填充
    plaintext = plaintext[:-plaintext[-1]]

    return plaintext.decode('utf-8')


# 测试
key = 'abcdefgh12345678abcdefgh'
plaintext = 'hello world!'
ciphertext = des3_encrypt(key, plaintext)
print('加密结果：', ciphertext)
plaintext = des3_decrypt(key, ciphertext)
print('解密结果：', plaintext)
