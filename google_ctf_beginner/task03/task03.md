> Thanks [0xf4b1](https://github.com/0xf4b1) so much for your solution, it helped me find my error and finish the task after 2 hours!
## Tools need to use:
JavaScript knowledge
## Solution:  
First, we go to the website in "WHAT YOU'LL NEED" part: https://high-speed-chase-web.2021.ctfcompetition.com/. This website requires us to write a JS script to control the car on the top of the screen, or what they call "Engage Re-programmed Self-Driving Mode!".  

We can see that:
- The function name is `controlCar`, and it required an array called `scanArray` given by the server, which containing 17 integers denoting distance from the car to the nearest obstacle.
- The position of indexes:
  - indexes 0-7 on the left side of the car (index 7 is the measurement at the left headlight)
  - index 8: at the center of the car
  - indexes 9-16: on the right side of the car (index 9 is the measurement at the right headlight)
- A negative measurement might appear if the obstacle is very close behind the car (this one is not necessary)
- Return value of function: 
  - `-1`: drive more to the left,
  - `0`: continue straight / straighten up the car,
  - `1`: drive more to the right.

There is also an explained version of the requirement: https://high-speed-chase-web.2021.ctfcompetition.com/task3explained.png

![image](https://user-images.githubusercontent.com/89294020/190450431-a42c1f7c-6597-4c4b-9498-ce63af397918.png)

Using those things, I make this JS script and it run perfectly!

```function controlCar(scanArray) {
    var max = scanArray[0];
    var maxind = 0;
    for (i = 0;i<17;i++){
        if (scanArray[i]>=max){ // fixed, before: scanArray[i]>max -> fail
            max = scanArray[i];
            maxind = i - 1; // i forgot to add this line of code -> wrong index
        }
    }
    if (maxind<8){
        return -1;
    } else if (maxind>8){
        return 1;
    } else {
        return 0;
}
}
```
When receive `scanArray` from server, the script will find the maximum value of those indexes, then find the first index that its value is <ins>**bigger or equal**</ins> to maximum value. (At first I only find the index bigger than maximum value -> wrong). Base on that, if that index if smaller than 8 then return `-1` -> make the car drive to the left, and so on.  

Finally, we get the flag: `CTF{cbe138a2cd7bd97ab726ebd67e3b7126707f3e7f}`
