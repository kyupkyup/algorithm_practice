const solution = (N, M, r, c, d, squareList) => {
  const direction = {
    1: [0, -1],
    2: [1, 0],
    3: [0, 1],
    0: [-1, 0],
  };

  while (true) {
    start = [c][r];
  }
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().split(' ').map(Number);
const [r, c, d] = input().split(' ').map(Number);
const squareList = [];
let flag = N;
while (flag--) {
  const square = input().split(' ').map(Number);
  squareList.push(square);
}
solution(N, M, r, c, d, squareList);
