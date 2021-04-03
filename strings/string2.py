# a3k2g7 -> adkmgn
#i9c5k4t1 -> irchko

seccode = input("seccode from agent sai srinivas athreya: ")
print(seccode)
decode = ""
seccodeLen = len(seccode)
for i in range(seccodeLen): #012345
    if i%2==1:
        decode = decode+ seccode[i-1]+chr(int(seccode[i])+ord(seccode[i-1]))   
if seccodeLen%2==1:
    decode = decode + seccode[-1]
print(decode)
