// function solution(times, k) {
//   const arr = [];
//   for (let i = 0; i < times.length; i++) {
//     arr.push([times[i], i + 1]);
//   }
//   arr.sort((a, b) => (a[0] - b[0] > 0 ? 1 : a[0] - b[0] < 0 ? -1 : a[1] - b[1] > 0 ? 1 : a[1] - b[1] < 0 ? -1 : 0));
//   let answer = arr[0][0];

//   while (k >= 0) {
//     if (arr.length === 0) {
//       return -1;
//     }
//     const numLeft = k - arr[0][0];
//     if (numLeft > 0) {
//       k = numLeft;
//       arr.shift();
//       arr.sort((a, b) => (a[0] - b[0] > 0 ? 1 : a[0] - b[0] < 0 ? -1 : a[1] - b[1] > 0 ? 1 : a[1] - b[1] < 0 ? -1 : 0));
//     } else if (numLeft === 0) {
//       return arr[0][1] + 1;
//     } else {
//       answer = arr[0][1] * arr.length;
//       k = numLeft;
//     }
//   }
//   return answer;
// }

// console.log(solution([1, 2, 3], 5));

// // let count = 0;
// // let pointer = 0;
// // while (true) {
// //   if (pointer === times.length) {
// //     pointer = 0;
// //   }
// //   let allDel = 0;
// //   while (times[pointer] === 0) {
// //     pointer += 1;
// //     if (pointer === times.length) {
// //       pointer = 0;
// //     }
// //     allDel += 1;
// //     if (allDel === times.length) return -1;
// //   }
// //   count += 1;
// //   if (count === k) break;

// //   times[pointer] -= 1;
// //   pointer += 1;
// // }
// // if (pointer === times.length) {
// //   pointer = 0;
// // }
// // return pointer + 1;
// // }

const solution = (nums, k) => {
  nums.unshift(0);
  const sT = nums.slice();
  sT.sort((a, b) => a - b);
  let rest = nums.length - 1;

  for (let i = 1; i < sT.length; i++) {
    if (k < rest * (sT[i] - sT[i - 1])) {
      // 끝난 경우
      const idx = k % rest;
      let cnt = 0;
      for (let j = 1; j < nums.length; j++) {
        if (nums[j] >= sT[i]) {
          if (cnt === idx) {
            return j;
          }
          cnt++;
        }
      }
    } else {
      k -= (rest * (sT[i] - sT[i - 1]));
      rest--;
    }
  }
  return -1;
};
console.log(solution([1, 2, 3], 5));
