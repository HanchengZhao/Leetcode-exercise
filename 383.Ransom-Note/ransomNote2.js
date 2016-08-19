/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
       var availableChars = {};

  for (var r = 0; r < magazine.length; r++) {
    var asciiCode = magazine.charCodeAt(r);
    availableChars[asciiCode] = (availableChars[asciiCode] || 0) + 1
  }

  for (var r = 0; r < ransomNote.length; r++) {
    var asciiCode = ransomNote.charCodeAt(r);
    availableChars[asciiCode] = (availableChars[asciiCode] || 0) - 1;
    // availableChars[asciiCode] will be greater than 0 if there is the same character in magazine
    
    if (availableChars[asciiCode] < 0) {
      console.log("failed at character " + String.fromCharCode(asciiCode));
      return false;
    }
  }

  return true;
};