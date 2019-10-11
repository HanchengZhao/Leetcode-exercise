/**
 * Initialize your data structure here.
 */
var Logger = function() {
  this.map = {};
};

/**
* Returns true if the message should be printed in the given timestamp, otherwise returns false.
      If this method returns false, the message will not be printed.
      The timestamp is in seconds granularity. 
* @param {number} timestamp 
* @param {string} message
* @return {boolean}
*/
Logger.prototype.shouldPrintMessage = function(timestamp, message) {
  if (message in this.map) {
    const print = timestamp - this.map[message] >= 10;
    if (print) {
      this.map[message] = timestamp;
    }
    return print;
  } else {
    this.map[message] = timestamp;
    return true;
  }
};
