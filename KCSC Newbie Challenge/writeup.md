## Link to post:
https://www.facebook.com/photo?fbid=122765970560556&set=a.120329284137558  
## Table of Contents
- [Information Gathering](#Information-Gathering)
- [Flags Discovering - Part 1](#Flags-Discovering---Part-1)
  - [flag1.txt](#flag1txt)
  - [flag2.txt](#flag2txt)
  - [flag3_4](#flag3_4)
  - [flag5_6.png](#flag5_6png)
- [Privilege Escalation - `mod`](#Privilege-Escalation---`mod`)
- [Flags Discovering - Part 2](#Flags-Discovering-Part-2)
  - [flag7.txt](#flag7txt)
- [Privilege Escalation - `admin`](#Privilege-Escalation---`admin`)
- [Flags Discovering - Part 3](#Flags-Discovering-Part-3)
  - [flag8.txt](#flag8txt)
- [Privilege Escalation - `root`](#Privilege-Escalation---`root`)
- [Flags Discovering - Part 4](#Flags-Discovering-Part-4)
  - [flag9.txt](#flag9txt)
  - [flag10.txt](#flag10txt)
  - [flag5.txt hardcore version](#flag5txt-hardcore-version)
  
  
## Information Gathering
- URL: http://chall.kcsc.cf:9000, password SSH: kcsc@123
- Directory `/home/user`:
```
total 112K
drwxr-xr-x 1 user user 4.0K Oct  7 15:00 .
drwxr-xr-x 1 root root 4.0K Oct  4 16:31 ..
lrwxrwxrwx 1 root root    9 Oct  4 16:22 .bash_history -> /dev/null
-rw-r--r-- 1 user user  220 Oct  4 16:22 .bash_logout
-rw-r--r-- 1 user user 3.7K Oct  4 16:22 .bashrc
drwx------ 2 user user 4.0K Oct  7 15:00 .cache
-rw-r--r-- 1 user user  807 Oct  4 16:22 .profile
-rw-r--r-- 1 root root   28 Oct  4 15:32 flag1.txt
-r-------- 1 root root   36 Oct  4 16:30 flag2.txt
drwxr-xr-x 2 root root 4.0K Oct  4 16:31 flag3_4
-rw-r--r-- 1 root root  47K Oct  4 15:32 flag5_6.png
-r-------- 1 root root   28 Oct  4 15:32 flag9.txt
-r--r--r-- 1 user user  17K Oct  4 16:22 read_flag2'
```
- Directory `/home/user/flag3_4`:
```
total 16K
-rw-r--r-- 1 root root   30 Oct  4 15:32 -
drwxr-xr-x 2 root root 4.0K Oct  4 16:31 .
drwxr-xr-x 1 user user 4.0K Oct  7 15:00 ..
-rw-r--r-- 1 root root   34 Oct  4 15:32 ...  
```
- Directory `/home/mod`:
```
total 28K
drwxr-xr-x 1 mod  mod  4.0K Oct  4 16:31 .
drwxr-xr-x 1 root root 4.0K Oct  4 16:31 ..
lrwxrwxrwx 1 root root    9 Oct  4 16:31 .bash_history -> /dev/null
-rw-r--r-- 1 mod  mod   220 Oct  4 16:31 .bash_logout
-rw-r--r-- 1 mod  mod  3.7K Oct  4 16:31 .bashrc
-rw-r--r-- 1 mod  mod   807 Oct  4 16:31 .profile
-r--r----- 1 mod  mod    31 Oct  4 15:32 flag7.txt
```
- Directory `/home/admin`:
```
drwxr-xr-x 1 admin admin 4.0K Oct  7 15:04 .
drwxr-xr-x 1 root  root  4.0K Oct  4 16:31 ..
lrwxrwxrwx 1 root  root     9 Oct  4 16:31 .bash_history -> /dev/null
-rw-r--r-- 1 admin admin  220 Oct  4 16:31 .bash_logout
-rw-r--r-- 1 admin admin 3.7K Oct  4 16:31 .bashrc
-rw-r--r-- 1 admin admin  807 Oct  4 16:31 .profile
-rw-r--r-- 1 admin admin    0 Oct  7 15:04 .sudo_as_admin_successful
-r--r----- 1 admin admin   30 Oct  4 15:32 flag8.txt
```
- Directory `/`:
```
bin  boot  dev  etc  flag10.txt  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```
## Flags Discovering - Part 1
### flag1.txt
### flag2.txt
### flag3_4
### flag5_6.png
## Privilege Escalation - `mod`
## Flags Discovering - Part 2
### flag7.txt
## Privilege Escalation - `admin`
## Flags Discovering - Part 3
### flag8.txt
## Privilege Escalation - `root`
## Flags Discovering - Part 4
### flag9.txt
### flag10.txt
### flag5.txt hardcore version
