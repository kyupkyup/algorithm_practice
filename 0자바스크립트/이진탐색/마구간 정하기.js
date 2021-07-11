const solution = (N, C, arr) => {
  arr.sort();
  let left = Math.min(...arr);
  const firstLeft = left;
  let right = Math.max(...arr);
  let answer = 0;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    let sum = firstLeft;
    let count = 1;
    let pointer = 0;
    sum += mid;
    while (pointer < N) {
      if (sum > arr[pointer]) {
        pointer += 1;
      } else {
        sum = arr[pointer] + mid;
        count += 1;
      }
    }
    if (count > C) {
      left = mid + 1;
    } else if (count < C) {
      right = mid - 1;
      answer = mid;
    } else {
      answer = mid;
      left += 1;
    }
  }
  return answer;
};

console.log(solution(5, 3, [1, 2, 8, 4, 9]));
