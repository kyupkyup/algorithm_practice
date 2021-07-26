// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  let sum = 0;
  let customSum = 0;
  for (let i = 1; i < A.length + 1; i++) {
    sum += i;
  }
  for (let i = 0; i < A.length; i++) {
    customSum += A[i];
  }
  if (Math.abs(sum - customSum) > 1000000000) return -1;
  return Math.abs(sum - customSum);
}

console.log(solution([6, 2, 3, 5, 6, 10000000000]));
