function solution(s1, s2) {
  const dp = [];

  for (let j = 0; j < s1.length + 1; j++) {
    const temp = [];
    for (let i = 0; i < s2.length + 1; i++) {
      temp.push(0);
    }
    dp.push(temp);
  }

  for (let j = 1; j < s1.length + 1; j++) {
    for (let i = 1; i < s2.length + 1; i++) {
      if (s1[j] === s2[i]) {
        if (dp[j - 1][i] <= i - 1 && dp[j][i - 1] <= j - 1) {
          dp[j][i] = dp[j - 1][i - 1] + 1;
        } else {
          dp[j][i] = Math.max(dp[j - 1][i], dp[j][i - 1]);
        }
      } else {
        dp[j][i] = Math.max(dp[j - 1][i], dp[j][i - 1]);
      }
    }
  }

  return dp[s1.length][s2.length];
}

console.log(solution('acbehf', 'abefc'));
