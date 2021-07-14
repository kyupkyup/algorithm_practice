function solution(nums, d, k) {
  let answer = Number.MIN_SAFE_INTEGER;
  const pow = Array.from({ length: d + 1 }, () => 0);
  const st = Array.from({ length: nums.length }, () => 0);
  pow[1] = 1;
  for (let i = 2; i <= d; i++) {
    pow[i] = pow[i - 1] * 2;
  }
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums[i].length; j++) {
      st[i] += pow[nums[i][j]];
    }
  }
  const check = [];
  for (let i = 0; i < d + 1; i++) {
    check.push(false);
  }

  const recur = (lev, bit) => {
    if (lev === k) {
      let count = 0;
      for (let i = 0; i < nums.length; i++) {
        if ((bit & st[i]) === st[i]) count += 1;
      }
      answer = Math.max(answer, count);
      return;
    }
    for (let i = 0; i < d + 1; i++) {
      if (!check[i]) {
        check[i] = true;
        recur(lev + 1, bit + pow[i]);
        check[i] = false;
      }
    }
  };
  recur(0, 0);
  return answer;
}

console.log(solution([[1], [2, 3], [3], [1, 2], [], [2, 1], [2, 3, 4], [3, 4]], 4, 3));

// 비트 마스킹으로 풀이
