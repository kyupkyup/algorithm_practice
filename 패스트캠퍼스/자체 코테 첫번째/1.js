const solution = s => {
  const ans = [];
  const check = {};
  let answer = '';
  for (let i = 0; i < s.length; i++) {
    if (!check[s[i]]) {
      check[s[i]] = 1;
      ans.push([s[i], 1]);
    } else {
      ans.forEach(item => {
        if (item[0] === s[i]) item[1] += 1;
      });
    }
  }

  ans.sort((a, b) => (b[1] - a[1]));

  for (let i = 0; i < ans.length; i++) {
    for (let j = 0; j < ans[i][1]; j++) {
      answer += ans[i][0];
      process.stdout.write(ans[i][0] + ' ');
    }
  }
  return answer;
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
