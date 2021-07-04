const solution = (N, M, r, c, d, squareList) => {
  let answer = 0;
  let gameSet = false;
  const direction = {
    1: [1, 0],
    2: [0, 1],
    3: [-1, 0],
    0: [0, -1],
  };
  const func = (r, c, d) => {
    if (gameSet) return;

    if (squareList[c][r] === 0) {
      answer += 1;
      squareList[c][r] = 2;
    }

    for (let i = 0; i < 4; i++) {
      d = d - 1 < 0 ? 3 : d - 1;
      const [moveX, moveY] = direction[d];
      if (squareList[c + moveY][r + moveX] === 0) {
        r += moveX;
        c += moveY;
        func(r, c, d);
      }
      if (gameSet) return;
    }

    let flag = false;
    for (let i = 0; i < 4; i++) {
      const [dx, dy] = direction[i];
      if (squareList[c + dy][r + dx] === 0) {
        flag = true;
      }
    }
    if (!flag && squareList[c - direction[d][1]][r - direction[d][0]] === 1) {
      gameSet = true;
    }
    if (gameSet) return;

    if (!flag) func(r - direction[d][0], c - direction[d][1], d);
  };
  func(c, r, d);
  return answer;
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
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
console.log(solution(N, M, r, c, d, squareList));
