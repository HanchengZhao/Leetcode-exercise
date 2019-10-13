/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var pacificAtlantic = function(matrix) {
  if (matrix.length == 0) return [];
  let res = [];
  let m = matrix.length,
    n = matrix[0].length;
  let pac = new Array(m).fill(null).map(() => new Array(n).fill(false));
  let atl = new Array(m).fill(null).map(() => new Array(n).fill(false));
  for (let i = 0; i < m; i++) {
    dfs(matrix, i, 0, pac, m, n);
    dfs(matrix, i, n - 1, atl, m, n);
  }
  for (let i = 0; i < n; i++) {
    dfs(matrix, 0, i, pac, m, n);
    dfs(matrix, m - 1, i, atl, m, n);
  }
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pac[i][j] && atl[i][j]) res.push([i, j]);
    }
  }
  return res;
};

function dfs(matrix, i, j, visited, m, n) {
  const directions = [[-1, 0], [0, 1], [0, -1], [1, 0]];
  visited[i][j] = true;
  for (let d of directions) {
    let nx = i + d[0],
      ny = j + d[1];
    if (
      nx < 0 ||
      nx >= m ||
      ny < 0 ||
      ny >= n ||
      visited[nx][ny] ||
      matrix[i][j] > matrix[nx][ny]
    )
      continue;

    dfs(matrix, nx, ny, visited, m, n);
  }
}

// the idea is to start from each ocean, do a dfs to see which
// areas will be flooded by water. Then check which areas can
// flow into both oceans.
