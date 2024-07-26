import base64
 
# 假设这是你的Base64编码过的字符串
encoded_string = "aGVsbG8gd29ybGQ="
encoded_string = "xm8WLl9H1EYgBCtli0yc7p4WdBGo0a2pPvfvSgYP0y9lOe+GnarRjbOrSqrRUgYhq6wf1TuzrBPNb8MFc+hcNsXMICJ+mg0NIildt62yXlLrwJNyd27jVA=="
 
# 解码Base64字符串
decoded_string = base64.b64decode(encoded_string)
 
# 输出解码后的字符串
print(decoded_string)
