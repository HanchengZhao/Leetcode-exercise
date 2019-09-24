var subsets = function(nums) {
  // either take it or not
  let res = [[]];
  for (let num of nums) {
    let temp = [];
    for (let sub of res) {
      temp.push(sub.concat([num]));
    }
    res = res.concat(temp);
  }
  return res;
};
