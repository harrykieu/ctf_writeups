# CutieK1tty
### Difficulty: Medium
> Một chú mèo cute chứa đựng nhiều điều bí ẩn. Hãy tìm ra điều thú vị đó.
### Tools used
- `exiftool`
- `binwalk`
- `Audacity`
- `hexeditor`
### Resources
[Here](./CutieK1tty/resources/stenography-003.zip) (password: `cookiehanhoan`)
### Solution
We are given a zip file, which contains a png file named `cut3_c4t.png`. Using `exiftool` to check the metadata of the image, we can see that there is some file hidden inside the image.
![0.png](./CutieK1tty/resources/images/0.png)
Using `binwalk` to extract the hidden file, we get a rar compressed file named `y0u_4r3_cl0s3.rar` and a mp3 file named `purrr_2.mp3`. 
![1.png](./CutieK1tty/resources/images/1.png)
The sound in the mp3 file is just some noise, so we cannot get any information from it. Using `Audacity` to check the spectrogram of the mp3 file, we can see a string inside the spectrogram: `sp3ctrum_1s_y0ur_fr13nd`.
![2.png](./CutieK1tty/resources/images/2.png)
We change our focus to the rar file. This file can not be opened, and using `exiftool` to check the metadata of the file, we can see that the file format is error.
![3.png](./CutieK1tty/resources/images/3.png)
Using `hexeditor` to check the header of the file, we can see that the header bytes are weird: `43 51 74 21` (CAT!) instead of `52 61 72 21` (RAR!). 
![4.png](./CutieK1tty/resources/images/4.png)
![5.png](./CutieK1tty/resources/images/5.png)
We change the header bytes to `52 61 72 21`:
![6.png](./CutieK1tty/resources/images/6.png)
and now we can open the rar file. The rar file contains a text file name `f1n4lly.txt`, which as its name suggests, can contain the final flag. 
![7.png](./CutieK1tty/resources/images/7.png)
Unfortunately, the file is password protected. And this is where the string we found in the spectrogram comes in handy. We use the string as the password, and we can open the file.
![8.png](./CutieK1tty/resources/images/8.png)
The flag is inside the file, but it is encoded in base64. We decode the string and get the flag:
![9.png](./CutieK1tty/resources/images/9.png)
The flag is `CHH{f0r3n51cs_ma5t3r}`.
