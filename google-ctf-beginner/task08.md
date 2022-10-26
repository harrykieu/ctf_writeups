# task08

### Tools need to use

* [pngtools](https://manpages.ubuntu.com/manpages/bionic/man1/pngchunks.1.html)

### Solution

Download and extract the zip file in the "WHAT YOU'LL NEED" part, we have a file called `hideandseek.png`.\
Using `pngcheck -v` to check the file, I found the suspect chunk name `eDIH` (maybe the name is reversed of `HIDe`?)

```
chunk eDIH at offset 0x00142, length 1:  illegal (unless recently approved) unknown, public chunk  
ERRORS DETECTED in image_directory
```

(Check out [this link](https://www.oreilly.com/library/view/png-the-definitive/9781565925427/17\_chapter-08.html) to get the idea of the chunk.)\
Using `pngchunks` to find the `eDIH` chunks, there are 48 chunks of that type. Each chunk has a data length of 1 byte, so maybe it represents a letter?

So, we should try to extract them and later convert+combine them into a normal string.

In the hex editor, we can find that 4 byte `65 44 49 48` (`b'\x65\x44\x49\x48'` in Python) represents the `eDIH` chunk indication, followed by 1 byte of data. I wrote a script to extract `eDIH` chunks' data and converted them to string:

```python
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


```

Running the script, we get the output: `Q1RGe0RpZFlvdUtub3dQTkdpc1Byb25vdW5jZWRQSU5HP30=`

The string ends with '=', so it is a string with `base64` format. Decode the string, we get the flag:\
`CTF{DidYouKnowPNGisPronouncedPING?}`
