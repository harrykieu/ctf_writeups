# Idea: const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));
# p: list below
# 0xcafe = 51966
# -> each letter of pass = each element of list - 51966 (0xcafe) -> conv to char using ASCII table
list = [52037,52077,52077,52066,52046,52063,52081,52081,52085,52077,52080,52066]
pwd = []
for a in list:
    pwd.append(chr(a-51966))
password = ''.join(pwd)
print(password)
# Website: https://cctv-web.2021.ctfcompetition.com
# Flag: CTF{IJustHopeThisIsNotOnShodan}