function solution(arr) {
  const n = arr.length;
  const maxDp = Array.from({ length: n }, () => 1);
  const minDp = Array.from({ length: n }, () => 1);
  const arrReversed = arr.slice().reverse();
  let answer = -1;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[i] >= arr[j]) {
        maxDp[i] = Math.max(maxDp[i], maxDp[j] + 1);
      }
    }
  }
  for (let k = 0; k < n; k++) {
    for (let m = 0; m < k; m++) {
      if (arrReversed[k] >= arrReversed[m]) {
        minDp[k] = Math.max(minDp[k], minDp[m] + 1);
      }
    }
  }
  minDp.reverse();
  for (let i = 0; i < n; i++) {
    answer = Math.max(answer, maxDp[i] + minDp[i] - 1);
  }

  return answer;
}
console.log(solution([6, 5, 1, 2, 1, 4, 5]));
