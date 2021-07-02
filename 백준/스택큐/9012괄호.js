const solution = (N, strList) => {
  for (let i = 0; i < N; i++) {
    let count = 0;
    for (let j = 0; j < strList[i].length; j++) {
      if (strList[i][j] === '(') count += 1;
      else if (strList[i][j] === ')') count -= 1;
      if (count < 0) break;
    }
    if (count !== 0) console.log('NO');
    else if (count === 0) console.log('YES');
  }
};

const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `3
((
))
())(()
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input(), 10);
const strList = [];
let flag = N;
while (flag--) {
  const str = input();
  strList.push(str);
}
solution(N, strList);
