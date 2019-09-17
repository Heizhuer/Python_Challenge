# 第一关: 更具图片解密解密str
# http://www.pythonchallenge.com/

a = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpqypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'qufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq()gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

text_translate = ''
for i in a:
    if str.isalpha(i):
        if i >= 'y':
            n = ord(i) + 2 - 26
        else:
            n = ord(i) + 2
        text_translate += chr(n)
    else:
        text_translate += i
print(text_translate)


# 官方答案
import string
b = string.ascii_lowercase
c = b[2:] + b[:2]
# 创建映射关系
d = str.maketrans(b, c)
print(d)
print(a.translate(d))
# 更具图片推出关键字为:
# 第二关链接:
