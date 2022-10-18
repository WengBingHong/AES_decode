import base64
from Crypto.Cipher import AES
from Crypto import Random
import os
import base64
import json



def decode_base64(data):
    missing_padding = 4-len(data)%4
    if missing_padding:
        data += b'='*missing_padding
    return (data)

###密文處理
def my_decode():

    #題目密文
    #16zvA3lnMuWHoE5PpaJheQ==
    message = b'16zvA3lnMuWHoE5PpaJheQ=='
    encrypt_data = message 
    encrypt_data = decode_base64(encrypt_data)

    ###解密處裡
    cipher = AES.new(key.encode('utf-8'),AES.MODE_ECB)
    result2 = base64.b64decode(encrypt_data)
    a = cipher.decrypt(result2)

    a = a.decode('utf-8','ignore')
    a = a.rstrip('\n')
    a = a.rstrip('\t')
    a = a.rstrip('\r')
    a = a.replace('\x06','')
    
    try:
        print('\n','data:',a)
        if(a[0] == 'H') and (a[1] == 'o'):
            fpp.write(key+"\t")
            fpp.write(a+'\n')
            fpp.flush()
    except:
        print("UnicodeEncodeError")

    # 第4組明文 : Ho

# 開啟檔案
fpp = open("anss.txt","w")

###金鑰處理
for a in range(33,127): 
    for b in range(33,127):
        for c in range(33,127):
            for d in range(33,127):
                print(a,b,c,d,end='')

                x1 = format(a, '02x')
                x2 = format(b, '02x')
                x3 = format(c, '02x')
                x4 = format(d, '02x')

                xx1 = bytes.fromhex(x1).decode("ASCII")
                xx2 = bytes.fromhex(x2).decode("ASCII")
                xx3 = bytes.fromhex(x3).decode("ASCII")
                xx4 = bytes.fromhex(x4).decode("ASCII")
                
                # 題目金鑰
                # s▆hv▆4z*▆7d*t▆Ce
                key = "s"+xx1+"hv"+xx2+"4z*"+xx3+"7d*t"+xx4+"Ce"
                # print(key)
                my_decode()

fpp.close()
