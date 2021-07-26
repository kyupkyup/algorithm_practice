function solution(A) {
  const freNum = new Map();
  for (let i = 0; i < A.length; i++) {
    if (freNum.has(A[i])) {
      freNum.set(A[i], freNum.get(A[i]) + 1);
    } else {
      freNum.set(A[i], 1);
    }
  }
  const sortedArr = [...freNum].sort((a, b) => (b[1] - a[1] > 0 ? 1 : b[1] - a[1] < 0 ? -1 : b[0] - a[0] >= 0 ? 1 : -1));
  for (const arr of sortedArr) {
    if (arr[0] === arr[1]) {
      return arr[0];
    }

    continue;
  }
  return 0;
}

console.log(solution([3, 8, 2, 3, 3, 2, 2]));
