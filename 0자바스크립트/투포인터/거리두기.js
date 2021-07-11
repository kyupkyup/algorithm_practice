// const solution = (N, arr) => {
//   let p1 = 0;
//   let answer = 0;
//   for (let p2 = 0; p2 < N; p2++) {
//     if (arr[p2] === 1) {
//       answer = Math.max(answer, Math.floor((p2 - p1) / 2));
//       p1 = p2;
//     }
//   }
//   return answer;
// };

const solution = (N, arr) => {
  const dp1 = [];
  const dp2 = [];
  let dist = 0;
  for (let i = 0; i < N; i++) {
    if (arr[i] === 0) {
      dist += 1;
      dp1.push(dist);
    } else {
      dist = 0;
      dp1.push(dist);
    }
  }
  for (let i = N - 1; i >= 0; i--) {
    if (arr[i] === 0) {
      dist += 1;
      dp2.push(dist);
    } else {
      dist = 0;
      dp2.push(dist);
    }
  }
  dp2.reverse();
  console.log(dp1);
  console.log(dp2);
};
// console.log(solution(18, [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1]));
console.log(solution(10, [1, 0, 0, 0, 1, 0, 0, 1, 0, 1]));
// console.log(solution(3, [1, 1, 1]));
// console.log(solution(3, [0, 0, 0, 1]));
// console.log(solution(3, [1, 0, 0, 0]));
