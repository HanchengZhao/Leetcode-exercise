/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    //seperate each character of a string and put them into array
    var ransomNoteChar = ransomNote.split('');
    var magazineChar = magazine.split('');
    //if the char in ransomNote is in magazine, remove it from the array 
    for(var i=0; i < ransomNoteChar.length; ++i){
        var char = ransomNoteChar[i];
        var index = magazineChar.indexOf(char);
        if(index > -1){
            magazineChar.splice(index,1);
        }else{
            return false;
        }
    };
    
    return true;
};


canConstruct("a", "b"); 
canConstruct("aa", "ab");
canConstruct("aa", "aab"); 