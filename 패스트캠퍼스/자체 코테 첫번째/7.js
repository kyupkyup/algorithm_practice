function solution(s1, s2) {
  const dp = [];

  for (let j = 0; j < s1.length + 1; j++) {
    const temp = [];
    for (let i = 0; i < s2.length + 1; i++) {
      if (i === 0) {
        temp.push(j);
      } else if (j === 0) {
        temp.push(i);
      } else {
        temp.push(0);
      }
    }
    dp.push(temp);
  }
  // j = s1
  // i = s2
  for (let j = 1; j < s1.length + 1; j++) {
    for (let i = 1; i < s2.length + 1; i++) {
      if (s1[j - 1] === s2[i - 1]) {
        dp[j][i] = dp[j - 1][i - 1];
      } else {
        dp[j][i] = Math.min(dp[j - 1][i], dp[j - 1][i - 1], dp[j][i - 1]) + 1;
      }
    }
  }
  return dp[s1.length][s2.length];
}
solution('acbehf', 'abefc');
solution('aabab', 'babb');
solution('', 'abefc');
