function solution(s) {
  // Write your code here

  const wordsMap = new Map();
  const wordsOnce = [];
  for (let i = 0; i < s.length; i++) {
    if (wordsMap.has(s[i])) wordsMap.set(s[i], wordsMap.get(s[i]) + 1);
    else wordsMap.set(s[i], 1);
  }
  for (const [key, value] of wordsMap) {
    if (value === 1) wordsOnce.push(key);
  }
  for (let i = 0; i < s.length; i++) {
    if (wordsOnce.includes(s[i])) return i + 1;
  }
  return -1;
}

console.log(solution('falafal'));
