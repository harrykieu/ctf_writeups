## Tools need to use
Chrome Developer Tool
## Solution
First, we go to the website in "WHAT YOU'LL NEED" part: https://cctv-web.2021.ctfcompetition.com  
Using Developer Tool to view the page source, we found the script with this snippet of code:
```const checkPassword = () => {
  const v = document.getElementById("password").value;
  const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));

  if(p[0] === 52037 &&
     p[6] === 52081 &&
     p[5] === 52063 &&
     p[1] === 52077 &&
     p[9] === 52077 &&
     p[10] === 52080 &&
     p[4] === 52046 &&
     p[3] === 52066 &&
     p[8] === 52085 &&
     p[7] === 52081 &&
     p[2] === 52077 &&
     p[11] === 52066) {
    window.location.replace(v + ".html");
  } else {
    alert("Wrong password!");
  }
}
```
As you can see, this is a JS script to check whether the password is correct or not.  
The line `const p = Array.from(v).map(a => 0xCafe + a.charCodeAt(0));` means that each element of the list `p` is each letter from the password, which will be converted into decimal number, then add the value of `0xCafe` in decimal (51966).  
Rearrange the elements of the list, I write a Python simple script to find the password (ex1.py)  
=> The password is: `GoodPassword`  
Enter the password, we will be redirected to another website with the flag: `CTF{IJustHopeThisIsNotOnShodan}`


