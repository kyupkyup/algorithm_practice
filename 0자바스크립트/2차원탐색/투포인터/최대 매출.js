const solution = (N, K, prices) => {
  let p1 = 0;
  let p2 = 0;
  //   let sum = prices.slice(0, 3).reduce((acc, i) => acc + i, 0);
  let sum = 0;
  let answer = 0;
  while (p2 < prices.length && p1 < prices.length) {
    if (p2 - p1 === K) {
      p1 += 1;
      sum += (prices[p2] - prices[p1 - 1]);
      answer = Math.max(answer, sum);
      p2 += 1;
    } else {
      sum += prices[p2];
      p2 += 1;
    }
  }
  return answer;
};

console.log(solution(10, 5, [12, 15, 11, 20, 25, 10, 20, 19, 13, 15]));
