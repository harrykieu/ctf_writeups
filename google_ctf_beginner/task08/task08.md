## Tools need to use
- [pngtools](https://manpages.ubuntu.com/manpages/bionic/man1/pngchunks.1.html)
## Solution
Download and extract the zip file in "WHAT YOU'LL NEED" part, we have a file called `hideandseek.png`.  
Using `pngcheck -v` to check the file, I found the suspect chunk name `eDIH` (maybe the name is reversed of HIDe?)
```
chunk eDIH at offset 0x00142, length 1:  illegal (unless recently approved) unknown, public chunk  
ERRORS DETECTED in image_directory
```
(Check out https://www.oreilly.com/library/view/png-the-definitive/9781565925427/17_chapter-08.html to get the idea of the chunk.)  
Using `pngchunks` to find the eDIH chunks, there are 48 chunks of that type (check in file `stats.txt`). Each chunk has data length of 1 byte, so maybe it represents a letter?  

So, we should try to extract them and later convert+combine them into a normal string.  

In hex editor, we can find that 4 byte `65 44 49 48` (`b'\x65\x44\x49\x48'` in Python) represents the eDIH chunk indication, follow by 1 byte of data. I wrote a script to extract eDIH chunks' data and converted them to string (`readedihchunk.py`).  

Running the script, we get the output: `Q1RGe0RpZFlvdUtub3dQTkdpc1Byb25vdW5jZWRQSU5HP30=`  
The string ends with '=', so it is a string with `base64` format. Decode the string, we get the flag:  
`CTF{DidYouKnowPNGisPronouncedPING?}`
