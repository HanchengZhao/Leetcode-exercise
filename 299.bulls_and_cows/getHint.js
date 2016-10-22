/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    var secretArray = secret.split("");
    var guessLeftArray = []
    var bulls = 0;
    var cows = 0;
    for(var i = 0; i < guess.length; i++){
        if(guess[i] === secret[i]){
            bulls++;
            var index = secretArray.indexOf(guess[i]);
            secretArray.splice(index,1);
        }else{
            guessLeftArray.push(guess[i]);
        }
    }
    for(var j = 0; j < guessLeftArray.length; j++){
       if(secretArray.indexOf(guessLeftArray[j]) !== -1){
            cows++;
            index = secretArray.indexOf(guessLeftArray[j]);
            secretArray.splice(index,1);
        }
    }
    return bulls + "A" + cows + "B";
};

console.log(getHint("1122","1222"));