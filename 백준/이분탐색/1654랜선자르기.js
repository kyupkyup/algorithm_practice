const solution = (K, N, lans) => {
  let left = 1;
  let right = Math.max(...lans);
  let mid = 0;

  while (left <= right) {
    let count = 0;
    mid = parseInt((left + right) / 2, 10);
    for (let i = 0; i < lans.length; i++) {
      count += parseInt(lans[i] / mid, 10);
    }

    if (count >= N) {
      left = mid + 1;
    } else if (count < N) {
      right = mid - 1;
    }
  }
  console.log(right);
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `4 11
802
743
457
539
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [K, N] = input().split(' ').map(Number);
const lans = [];
let flag = K;
while (flag--) {
  const lan = parseInt(input(), 10);
  lans.push(lan);
}
solution(K, N, lans);
