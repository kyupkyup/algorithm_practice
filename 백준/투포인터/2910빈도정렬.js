const solution = (N, C, arr) => {
  const ans = [];
  const check = {};
  for (let i = 0; i < arr.length; i++) {
    if (!check[arr[i]]) {
      check[arr[i]] = 1;
      ans.push([arr[i], 1]);
    } else {
      ans.forEach(item => {
        if (item[0] === arr[i]) item[1] += 1;
      });
    }
  }

  ans.sort((a, b) => (b[1] - a[1]));

  for (let i = 0; i < ans.length; i++) {
    for (let j = 0; j < ans[i][1]; j++) {
      process.stdout.write(ans[i][0] + ' ');
    }
  }
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `9 77
11 33 11 77 54 11 25 25 33
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, C] = input().split(' ').map(Number);
const arr = input().split(' ');
solution(N, C, arr);
