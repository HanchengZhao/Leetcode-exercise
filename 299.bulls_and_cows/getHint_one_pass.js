var getHint = function(secret, guess) {
    var numbers = [];
    for(var j = 0; j < 10; j++){
        numbers[j] = 0;
    }//initialize array
    var bulls = 0;
    var cows = 0;
    for(var i = 0; i < secret.length; i++){
        var g = guess[i];
        var s = secret[i];
        if(s === g){
            bulls++;
        }else{
            if(numbers[g] < 0) cows++;
            if(numbers[s] > 0) cows++;
            numbers[s]--;
            numbers[g]++;
        }
    }
    return bulls + "A" + cows + "B";
};

console.log(getHint("1122","1222"));