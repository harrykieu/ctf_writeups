So, one of my friends at the university sent me a link to a Facebook post about a CTF challenge for fresher of the KMA CS Club. After nearly 4 hours of playing this challenge (half of the time I went in the wrong way LOL), I finally passed. Here is my write-up on how to solve it.  
## Link to post:
https://www.facebook.com/photo?fbid=122765970560556&set=a.120329284137558  
## Table of Contents
- [Information Gathering](#Information-Gathering)
- [Flags Discovering - Part 1](#Flags-Discovering---Part-1)
  - [flag1.txt](#flag1txt)
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
  - [flag2.txt](#flag2txt)
  - [flag9.txt](#flag9txt)
  - [flag10.txt](#flag10txt)
  - [flag5.txt hardcore version](#flag5txt-hardcore-version)
  
## Information Gathering
- Connect: `ssh user@chall.kcsc.cf -p XXXXX`, password SSH: `kcsc@123`
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
Simply use the command `cat flag1`, we get the flag: `KCSC{part_1_read_file_4zs0}`
### flag3_4
- flag3: Using `ls -lah` to list all the file in `flag3_4` folder, we see a file with the name `-`. Using command `cat ./-`, we get the flag: `KCSC{part_3_read_file_strike}`  
- flag4: We can also see that in this folder, there is a file name `...`. Using command `cat ./...`, we get the flag: `KCSC{part_4_read_file_quadra_dot}`
### flag5_6.png
- flag6: By checking strings in the image file: `strings flag5_6.png`, we get the flag: `KCSC{part_6_read_me_pls}`
- flag5: There are 2 ways to get this flag:
1. Because we cannot display the png using the terminal without any tool, we must somehow have this file in our computer, which allows us to see the image file. To do so, first, we must copy the image file to the `/tmp` folder to be able to copy this file: `cp flag5_6.png /tmp`. Then, in our machine's terminal, using `scp` command to copy this file to our computer: `scp -P XXXXX user@chall.kcsc.cf:/tmp/flag5_6.png /tmp`. Open this file, we get the flag: `KCSC{part_5_u_know_scp}`  
  2. At first, I don't remember the `scp` way, so my idea is to get the `root` privilege, then install some tool to read the image's content directly in the terminal. This idea will take a very long time (we must get the `root` privilege first), but it is possible as you will see later. 
  
## Privilege Escalation - `mod`
We return back to `/home` to check how many users are available on this machine. The remaining 2 users are `mod` and `admin`, and each user's `home` folder has a flag file which only that user can open. So, we must somehow "become" those users to be able to read those flag. Checking `sudo -l` for any exploitable vulnerabilities:
```
user@kcsc:~$ sudo -l
Matching Defaults entries for user on kcsc:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user may run the following commands on kcsc:
    (root) NOPASSWD: /home/user/read_flag2
    (mod) NOPASSWD: /usr/bin/env
```
Searching on [gtfobin](https://gtfobins.github.io), we see that `env` binary can be used for privilege escalation, as this can be run as `mod` user without requiring any password. So, we try to spawn a shell with `mod` privilege using `env`: `sudo -u mod env /bin/bash`, and now we have become `mod`!
## Flags Discovering - Part 2
### flag7.txt
Now, we can simply `cat flag7.txt` to get the flag: `KCSC{part_7_wow_u_r_quite_gud}`
## Privilege Escalation - `admin`
The only user left 
## Flags Discovering - Part 3
### flag8.txt
## Privilege Escalation - `root`
## Flags Discovering - Part 4
### flag2.txt
### flag9.txt
### flag10.txt
### flag5.txt hardcore version
