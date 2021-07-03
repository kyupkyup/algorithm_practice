function solution(nums, m) {
  let answer = 0;
  const minus = m => {
    if (m === 0) {
      answer += 1;
      return;
    }

    for (const number of nums) {
      if (m - number < 0) continue;
      minus(m - number);
    }
  };
  minus(m);
  return answer;
}

console.log(solution([2, 3, 5], 10));
