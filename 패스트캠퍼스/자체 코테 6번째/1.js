function solution(nums) {
  let answer = 0;

  for (let i = 0; i < nums.length; i++) {
    let pointer = i;
    let count = 1;
    while (true) {
      if (nums[i] > nums[pointer + 1]) count += 1;
      else {
        answer = Math.max(answer, count);
        break;
      }
      pointer += 1;
    }
  }
  return answer;
}

solution([3, 5, 8, 7, 6, 9, 12, 15]);
