'''
Avoid looking for spoilers.

Forums: Python Challenge Forums, read before you post.
IRC: irc.freenode.net #pythonchallenge

Version : Python 3.7.4

'''

input_texts = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input_texts = list(input_texts)
result=""

n=0
for i in input_texts:
    if input_texts[n] < "a":
        result = result+chr(ord(input_texts[n]))
    elif input_texts[n] > "z":
        result = result+chr(ord(input_texts[n]))
    else:
        if input_texts[n] == "y":
            result = result+"a"
        elif input_texts[n] == "z":
            result = result+"b"
        elif input_texts[n] == " ":
            result = result+" "
        else:
            result = result+chr(ord(input_texts[n])+2)
    n=n+1

print(result)
