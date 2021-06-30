const calculate = (i, j, elements) => {
  let ans = -1;
  // 행
  let count = 0;
  for (let flag = 0; flag < elements.length; flag++) {
    count += elements[j][flag];
  }
  if (count > ans) ans = count;
  count = 0;
  // 열
  for (let flag = 0; flag < elements.length; flag++) {
    count += elements[flag][i];
  }
  if (count > ans) ans = count;
  count = 0;
  // 오른 대각선
  let [x, y] = [i, j];
  while (x >= 0 && y >= 0) {
    count += elements[y][x];
    x -= 1;
    y -= 1;
  }
  [x, y] = [i + 1, j + 1];
  while (x < elements.length && y < elements.length) {
    count += elements[y][x];
    x += 1;
    y += 1;
  }
  if (count > ans) ans = count;
  count = 0;
  // 왼 대각선

  [x, y] = [i, j];
  while (x >= 0 && y < elements.length) {
    count += elements[y][x];
    x -= 1;
    y += 1;
  }
  [x, y] = [i + 1, j - 1];
  while (x < elements.length && y >= 0) {
    count += elements[y][x];
    x += 1;
    y -= 1;
  }
  if (count > ans) ans = count;
  return ans;
};
const solution = (K, elements) => {
  let ans = -1;
  for (let j = 0; j < K; j++) {
    for (let i = 0; i < K; i++) {
      const temp = calculate(i, j, elements);
      ans = ans > temp ? ans : temp;
    }
  }
  console.log(ans);
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const K = parseInt(input(), 10);
const elements = [];
let flag = K;
while (flag--) {
  const element = input().split(' ').map(Number);
  elements.push(element);
}
solution(K, elements);
