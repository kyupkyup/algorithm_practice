const solution = (M, N, squareList) => {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, -1, 1];

  const squareLegend = [];
  for (let i = 0; i < M; i++) {
    const tempArr = [];
    for (let j = 0; j < N; j++) {
      tempArr.push(false);
    }
    squareLegend.push(tempArr);
  }
  for (const square of squareList) {
    const yStart = M - square[1];
    const yEnd = M - square[3];
    for (let x = square[0]; x < square[2]; x++) {
      for (let y = yStart > yEnd ? yEnd : yStart; y < (yStart > yEnd ? yStart : yEnd); y++) {
        squareLegend[y][x] = true;
      }
    }
  }
  const queue = [];
  let count = 0;
  const ans = [];
  for (let j = 0; j < M; j++) {
    for (let i = 0; i < N; i++) {
      if (squareLegend[j][i]) continue;
      squareLegend[j][i] = true;
      queue.push([i, j]);
      count += 1;
      let width = 1;
      while (queue.length > 0) {
        const [x, y] = queue.shift();
        for (let k = 0; k < 4; k++) {
          const nx = x + dx[k];
          const ny = y + dy[k];
          if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (!squareLegend[ny][nx]) {
              queue.push([nx, ny]);
              squareLegend[ny][nx] = true;
              width += 1;
            }
          }
        }
      }
      ans.push(width);
    }
  }
  console.log(count);
  console.log(ans.sort((a, b) => a - b).join(' '));
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

const [M, N, K] = input().split(' ').map(Number);
const squareList = [];
let flag = K;
while (flag--) {
  const square = input().split(' ').map(Number);
  squareList.push(square);
}
solution(M, N, squareList);
