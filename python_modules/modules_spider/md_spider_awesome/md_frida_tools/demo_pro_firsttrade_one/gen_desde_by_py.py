from Crypto.Cipher import DES3


# �������һ��ʹ��Python����ʵ��3DES�����㷨�����̣���Ҫʹ��pycryptodome�����֧�֡��������£�
def des3_encrypt(key, plaintext):
    key = key.encode('utf-8')
    plaintext = plaintext.encode('utf-8')

    # �������
    length = 8 - (len(plaintext) % 8)
    plaintext += bytes([length]) * length

    # ��ʼ��������
    cipher = DES3.new(key, DES3.MODE_CBC, b'\0' * 8)

    # ����
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext


def des3_decrypt(key, ciphertext):
    key = key.encode('utf-8')

    # ��ʼ��������
    cipher = DES3.new(key, DES3.MODE_CBC, b'\0' * 8)

    # ����
    plaintext = cipher.decrypt(ciphertext)

    # ȥ�����
    plaintext = plaintext[:-plaintext[-1]]

    return plaintext.decode('utf-8')


# ����
key = 'abcdefgh12345678abcdefgh'
plaintext = 'hello world!'
ciphertext = des3_encrypt(key, plaintext)
print('���ܽ����', ciphertext)
plaintext = des3_decrypt(key, ciphertext)
print('���ܽ����', plaintext)
