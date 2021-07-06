const solution = s => {
  const ans = [];
  const check = new Map();
  let answer = '';
  for (let i = 0; i < s.length; i++) {
    if (!check.has(s[i])) {
      check.set(s[i], 1);
    } else {
      check.set(s[i], check.get(s[i]) + 1);
    }
  }
  const checked = [...check].sort((a, b) => b[1] - a[1]);
  console.log(checked);

  for (let i = 0; i < checked.length; i++) {
    for (let j = 0; j < checked[i][1]; j++) {
      answer += checked[i][0];
    }
  }
  return answer;
};

console.log(solution('ABCCAaABBCCAAab'));
