function solution(nums, k) {
  let answer = 0;
  let p1 = 0;
  let flag = 0;

  for (let p2 = 0; p2 < nums.length; p2++) {
    if (nums[p2] === 0) flag++;
    while (flag > k) {
      if (nums[p1] === 0) flag--;
      p1++;
    }
    answer = Math.max(answer, p2 - p1 + 1);
  }
  return answer;
}

console.log(solution([0, 0, 1, 0, 0], 0));
console.log(solution([0, 0, 1, 0, 1], 3));
console.log(solution([1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], 2));
console.log(solution([0, 0, 0, 0, 0], 2));
