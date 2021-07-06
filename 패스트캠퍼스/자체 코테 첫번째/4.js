// function solution(nums, m) {
// let answer = 0;
// const minus = m => {
//   if (m === 0) {
//     answer += 1;
//     return;
//   }

//   for (const number of nums) {
//     if (m - number < 0) continue;
//     minus(m - number);
//   }
// };
// minus(m);
// return answer;
// }
function solution(nums, m) {
  const answer = 0;
  const dp = [];
  for (let i = 0; i < m + 1; i++) {
    dp.push(0);
  }
  dp[0] = 1;

  for (let i = 1; i < m + 1; i++) {
    for (const coin of nums) {
      if (i - coin >= 0) {
        dp[i] += dp[i - coin];
      }
    }
  }
  return dp[dp.length - 1];
}
console.log(solution([2, 3, 5], 10));
