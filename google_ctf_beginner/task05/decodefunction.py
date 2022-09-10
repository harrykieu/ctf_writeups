from fileinput import close
import random
from randcrack import RandCrack
import binascii

#Generate a RandCrack instance
rc = RandCrack()

#Supply the random numbers to RandCrack
with open("D:/googlectfbeginner/task05/number.txt") as f:
    for line in f:
        rc.submit(int(line.strip())-(1 << 31)) #must minus 1<<31
    close()

#Predict the pre-generated key
key = []
for i in range(0, 31):
    key.append(rc.predict_getrandbits(8))

#Read the bytes in secret.enc 1 by 1
ba = bytearray()
with open("D:/googlectfbeginner/task05/secret.enc", "rb") as f:
    byte = f.read(1)
    while byte:
        ba += byte
        byte = f.read(1)

#Decode the secret
#Reverse function of XOR is XOR itself
print(bytes([a ^ b for a, b in zip(key, ba)]))
