import base64

# Create an array of the binary of png file, each element is 1 byte
with open("task08/hideandseek.png","rb") as f:
    obj = f.read()
    list1 = [obj[i:i+1] for i in range(len(obj))]

#Find the eDIH chunk in array
list2 = []
for i in range(len(list1)):
    #b'\x65\x44\x49\x48' = eDIH
    if list1[i] == b'\x65' and list1[i+1] == b'\x44' and list1[i+2]==b'\x49' and list1[i+3]==b'\x48': 
        list2.append(list1[i+4]) #each eDIH chunk has 1 byte data


# Decode the binary in eDIH chunks into string 
str = "".join([i.decode("utf-8") for i in list2])
print(str)
# => Output: Q1RGe0RpZFlvdUtub3dQTkdpc1Byb25vdW5jZWRQSU5HP30= -> base64 encode

# Decode into normal string
print(base64.b64decode(str))
# Output: b'CTF{DidYouKnowPNGisPronouncedPING?}'


