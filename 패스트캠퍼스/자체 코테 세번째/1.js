const solution = (nums, K) => {
  let p1 = 0;
  let p2 = K;
  const answer = [];
  const map = new Map();
  for (let i = p1; i < p2; i++) {
    if (map.has(nums[i])) map.set(nums[i], map.get(nums[i]) + 1);
    else map.set(nums[i], 1);
  }
  p1 += 1;

  answer.push(map.size);
  while (p2 < nums.length) {
    if (map.get(nums[p1 - 1]) > 1) map.set(nums[p1 - 1], map.get(nums[p1 - 1]) - 1);
    else map.delete(nums[p1 - 1]);

    if (map.has(nums[p2])) map.set(nums[p2], map.get(nums[p2]) + 1);
    else map.set(nums[p2], 1);
    answer.push(map.size);
    p1 += 1;
    p2 += 1;
  }
  return answer;
};

console.log(solution([20, 12, 20, 10, 23, 17, 10], 4));
