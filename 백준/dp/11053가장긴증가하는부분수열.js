const solution = (M, numList) => {
  const dp = [];
  for (let i = 0; i < M; i++) {
    dp.push(1);
  }
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < i; j++) {
      if (numList[i] > numList[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }
  console.log(Math.max(...dp));
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `6
10 20 10 30 20 50
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const M = parseInt(input(), 10);
const numList = input().split(' ').map(Number);

solution(M, numList);
