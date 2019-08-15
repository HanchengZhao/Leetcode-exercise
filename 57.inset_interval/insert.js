/**
 * Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 * You may assume that the intervals were initially sorted according to their start times.
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */

// loop through the array and find the lower bound and higher bound
// then merge the interval
// the difficult part is handling the insert, should only increase the insert index
// when the newInterval is behind the interval traversed
var insert = function(intervals, newInterval) {
  const newArray = [];
  let insertIndex = 0;
  for (let i = 0; i < intervals.length; i++) {
    // no overlap
    if (newInterval[0] > intervals[i][1]) {
      newArray.push(intervals[i]);
      insertIndex++;
    } else if (newInterval[1] < intervals[i][0]) {
      newArray.push(intervals[i]);
    } else {
      newInterval = [
        Math.min(newInterval[0], intervals[i][0]),
        Math.max(newInterval[1], intervals[i][1]),
      ];
    }
  }
  newArray.splice(insertIndex, 0, newInterval);
  return newArray;
};
