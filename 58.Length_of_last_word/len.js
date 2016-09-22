/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    if(s === ""){
        return 0;
    }
    var arr = s.split(' ');
    console.log('arr:' + arr);
    var lastWord;
    for(var i = arr.length - 1; i > 0; i--){
        if (arr[i] !== '' && arr[i] !== ' ' ){
            lastWord = arr[i];
            console.log((arr[i]));
            break;
        }
    }
    
    if(lastWord === undefined){//if s is a word
        console.log(s.length);
        return s.length
    }else{
        console.log(lastWord);
        console.log(lastWord.length);
        return lastWord.length;
    }
  
};

lengthOfLastWord(" ");