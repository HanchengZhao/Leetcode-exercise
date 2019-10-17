/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
  if (!wordList.includes(endWord)) {
    return 0
  }
  let queue = [beginWord];
  let wordSet = new Set(wordList);
  let seen = new Set(queue);
  let steps = 1;
  while (queue.length) {
    let next = [];
    for (let w of queue) {
      if (w === endWord) return steps;
      for (let i = 0; i < w.length; i++) {
        for (let j = "a".charCodeAt(0); j <= "z".charCodeAt(0); j++) {
          const newWord = w.substring(0, i) + String.fromCharCode(j) + w.substring(i + 1);
          if (!seen.has(newWord) && wordSet.has(newWord)) {
            next.push(newWord);
            seen.add(newWord)
          }
        }
      }
    }

    steps++;
    queue = next
  }
  return 0;
};