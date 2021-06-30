const solution = times => {
  times.sort((a, b) => (a[1] < b[1] ? -1 : a[1] > b[1] ? 1 : a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0));
  let count = 0;
  let endTime = -1;
  for (const time of times) {
    if (time[0] >= endTime) {
      [, endTime] = time;
      count += 1;
    }
  }
  console.log(count);
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `5
0 1
1 2
2 2
2 3
3 3
`
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let t = input();
const times = [];

while (t--) {
  const [a, b] = input().split(' ').map(Number);
  times.push([a, b]);
}
solution(times);
