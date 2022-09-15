//source: https://0xf4b1.github.io/ctftime/gctf-2021-beginners/3-moscow-streets/
function controlCar(scanArray) {
    var max = scanArray[0];
    var maxind = 0;
    for (i = 0;i<17;i++){
        if (scanArray[i]>=max){                 // fixed, before: scanArray[i]>max -> wrong
            max = scanArray[i];
            maxind = i - 1;                     // i forgot to add this line of code
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
