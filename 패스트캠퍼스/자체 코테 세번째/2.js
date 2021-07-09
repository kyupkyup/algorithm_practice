function solution(nums, h) {
  let left = 1;
  let right = Math.max(...nums);
  let mid = 0;
  while (left < right) {
    mid = Math.ceil((left + right) / 2);
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
      sum += Math.ceil(nums[i] / mid);
    }
    if (sum > h) {
      left = mid + 1;
    } else if (sum < h) {
      right = mid - 1;
    } else if (sum === h) {
      right -= 1;
    }
  }
  return mid;
}
console.log(solution([29, 12, 24, 5, 19], 6));
