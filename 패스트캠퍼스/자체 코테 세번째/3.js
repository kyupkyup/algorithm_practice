// function solution(nums, m) {
//   let answer = 0;
//   let p1 = 0;
//   let p2 = 0;
//   let sum = 0;

//   for (let i = p1; i < p2 + 1; i++) {
//     sum += nums[i];
//   }
// while (p2 < nums.length) {
//   if (sum > m) {
//     sum -= nums[p1];
//     p1 += 1;
//   } else if (sum < m) {
//     p2 += 1;
//     sum += nums[p2];
//   } else if (sum === m) {
//     answer += 1;
//     sum -= nums[p1];
//     p1 += 1;
//     p2 += 1;
//     sum += nums[p2];
//   }
// }

//   return answer;
// }

// console.log(solution([1, 2, 1, 3, 1, 1, 1, 2], 6));
// console.log(solution([1, 1, 1, 1], 3));

// const solution = num => {
//   const nums = [];
//   for (let i = 1; i <= num; i++) {
//     nums.push(i);
//   }
//   let answer = 0;
//   let p1 = 0;
//   let p2 = 0;
//   let sum = nums[p2];

//   while (p2 < nums.length) {
//     if (sum > num) {
//       sum -= nums[p1];
//       p1 += 1;
//     } else if (sum < num) {
//       p2 += 1;
//       sum += nums[p2];
//     } else if (sum === num) {
//       let temp_p1 = p1;
//       let flag = false;
//       while (p2 !== temp_p1) {
//         if (nums[temp_p1 + 1] - 1 !== nums[temp_p1]) {
//           flag = true;
//           break;
//         }
//         temp_p1 += 1;
//       }
//       if (!flag) answer += 1;
//       sum -= nums[p1];
//       p1 += 1;
//       p2 += 1;
//       sum += nums[p2];
//     }
//   }
//   return answer - 1;
// };
// console.log(solution(16));
// console.log(solution([1, 1, 1, 1], 3));

const solution = num => {

};
solution(15);
