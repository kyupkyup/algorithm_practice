function solution(arr) {
  const n = arr.length;
  let answer = 0;
  let pointer = 0;
  for (let i = 0; i < n; i++) {
    if (answer > n - i) return answer;
    let flag = 'up';
    pointer = i;
    while (flag === 'up') {
      if (pointer + 1 >= n) {
        flag = 'down';
        break;
      }

      if (arr[pointer + 1] >= arr[pointer]) {
        pointer += 1;
      } else {
        flag = 'down';
      }
    }
    while (flag === 'down') {
      if (pointer + 1 >= n) {
        answer = Math.max(answer, pointer - i + 1);
        break;
      }

      if (arr[pointer + 1] <= arr[pointer]) {
        pointer += 1;
      } else {
        answer = Math.max(answer, pointer - i + 1);
        break;
      }
    }
  }
  return answer;
}
console.log(solution([5, 9, 7, 6, 2, 1]));
