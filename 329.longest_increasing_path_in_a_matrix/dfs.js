/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
  if (matrix.length === 0) return 0;
  let m = matrix.length,
    n = matrix[0].length;
  // init 2d array with -1, cached longest increasing path at this pos
  let cache = new Array(m).fill(null).map(() => new Array(n).fill(-1));
  let longest = 1;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      longest = Math.max(longest, dfs(matrix, i, j, cache, m, n));
    }
  }
  return longest;
};

function dfs(matrix, i, j, cache, m, n) {
  if (cache[i][j] !== -1) return cache[i][j];
  let res = 1;
  const directions = [[-1, 0], [0, 1], [0, -1], [1, 0]];
  for (let d of directions) {
    let nx = i + d[0],
      ny = j + d[1];
    if (
      nx < 0 ||
      nx >= m ||
      ny < 0 ||
      ny >= n ||
      matrix[i][j] <= matrix[nx][ny]
    )
      continue;
    res = Math.max(res, 1 + dfs(matrix, nx, ny, cache, m, n));
  }
  cache[i][j] = res;
  return res;
}
