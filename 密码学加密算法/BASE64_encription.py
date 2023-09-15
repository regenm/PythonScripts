import base64 
 
#加密
print("encoding= utf-8")
str1 = input("input:")
b = base64.b64encode(str1.encode('utf-8')).decode("utf-8") 
print("encripted result:",b) 
 
#解密 
c = base64.b64decode(b.encode("utf-8")).decode("utf-8") 
print("decripted result:",c)
 
 
