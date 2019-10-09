/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
  let jumps = 0,
    start = 0,
    end = 0,
    furthest = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    furthest = Math.max(furthest, i + nums[i]);
    if (i == end) {
      jumps++;
      end = furthest;
    }
  }
  return jumps;
};
