/*
'''
1. ⼀一个矩阵，只有0和1，找到⾥里里⾯面全为1的矩形的坐标。输⼊入⼀一定有效，保 证有⼀一个满⾜足要求的矩形。⽤用左上和右下坐标表示
⽐比如:
0 0 0 0 0. ⽜牛⼈人云集,⼀一亩三分地
0 1 1 0 0. more info on 1point3acres 00000
结果就是返回
[1,1], [1,2]
2. follow up 有很多个这样的矩形， 返回所有的矩形的左上右下坐标 3. 不不⼀一定是矩形，找出所有连通的1. . from: 1point3acres
10011
00011
10001
这样的输⼊入，返回⼀一个⼤大数组
[
[0,0],
[[0,3], [0,4], [1,3], [1,4], [2,4]], [2,1]
]
*/

const rect1 = [
  [1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 1],
  [1, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
];

function getRectPos(arr) {
  if (arr.length === 0) {
    return [];
  }
  const row = arr.length;
  const col = arr[0].length;
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (arr[i][j] === 0) {
        let rowEnd = i;
        let colEnd = j;
        while (rowEnd < row && arr[rowEnd][j] == 0) {
          rowEnd++;
        }
        while (colEnd < col && arr[i][colEnd] == 0) {
          colEnd++;
        }
        return [[i, j], [rowEnd - 1, colEnd - 1]];
      }
    }
  }
}
// console.log(getRectPos(rect1));

const input2 = [
  [1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 1, 1],
  [0, 0, 1, 0, 0, 0],
  [1, 1, 1, 0, 1, 0],
  [1, 0, 0, 1, 1, 1],
];
function getAllPos(arr) {
  if (arr.length === 0) {
    return [];
  }
  let res = [];
  const row = arr.length;
  const col = arr[0].length;
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (arr[i][j] === 0) {
        const start = [i, j];
        let rowEnd = i;
        let colEnd = j;
        while (colEnd + 1 < col && arr[i][colEnd + 1] === 0) {
          colEnd += 1;
        }
        while (rowEnd + 1 < row && arr[rowEnd + 1][j] === 0) {
          rowEnd += 1;
        }
        const end = [rowEnd, colEnd];

        res.push([start, end]);
        visited(arr, start, end);
      }
    }
  }
  return res;
}

function visited(arr, pos1, pos2) {
  for (let i = pos1[0]; i <= pos2[0]; i++) {
    for (let j = pos1[1]; j <= pos2[1]; j++) {
      arr[i][j] = 1;
    }
  }
}
console.log(getAllPos(input2));

function groupPos(arr) {
  let res = [];
  let row = arr.length;
  let col = arr[0].length;
  for(let i = 0;)
}