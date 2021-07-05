function solution(s) {
  const strSet = new Set();
  const RealAnswer = new Map();
  const findRight = s => {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
      if (s[i] === '(') {
        count += 1;
      } else if (s[i] === ')') {
        count -= 1;
        if (count < 0) {
          break;
        }
      }
    }
    if (count !== 0) return false;
    return true;
  };

  const dfs = (delChar, str, countingNum) => {
    if (str === '') return;
    const newStr = str.substring(0, delChar) + str.substring(delChar + 1);

    if (strSet.has(newStr) || newStr === '') return;
    strSet.add(newStr);

    if (findRight(newStr)) {
      if (RealAnswer.has(countingNum)) RealAnswer.set(countingNum, RealAnswer.get(countingNum) + 1);
      else RealAnswer.set(countingNum, 1);
      return;
    }
    for (let i = 0; i < newStr.length; i++) {
      dfs(i, newStr, countingNum + 1);
    }
  };

  const countingNum = 1;

  for (let i = 0; i < s.length; i++) {
    dfs(i, s, countingNum);
  }
  console.log([...RealAnswer].sort((a, b) => a[0] - b[0]));
  if (RealAnswer.size === 0) return 0;
  return [...RealAnswer].sort((a, b) => a[0] - b[0])[0][1];
}

console.log(solution(')'));
