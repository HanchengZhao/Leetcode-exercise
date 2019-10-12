/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
  const N = board.length;
  let q = [1];
  let positions = { "1": 0 };
  while (q.length > 0) {
    let n = q.shift();
    if (n == N * N) return positions[n];
    for (let i = n + 1; i <= Math.min(n + 6, N * N); i++) {
      const [r, c] = getLoc(i);
      const next = board[r][c] === -1 ? i : board[r][c];
      // only record the step on the first reach
      if (positions[next] === undefined) {
        q.push(next);
        positions[next] = positions[n] + 1;
      }
    }
  }
  return -1;
};

function getLoc(pos, N) {
  let row = Math.floor((pos - 1) / N);
  let col = (pos - 1) % N;
  col = row % 2 === 1 ? N - col - 1 : col;
  row = N - row - 1;
  return [row, col];
}

console.log(
  snakesAndLadders([
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
  ])
);
