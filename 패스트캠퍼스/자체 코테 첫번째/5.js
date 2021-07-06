// const score = (arr1, cans) => {
//   let white1 = 0;
//   let black1 = 0;
//   let white2 = 0;
//   let black2 = 0;
//   arr1.sort((a, b) => b - a);
//   for (let i = 0; i < arr1.length; i++) {
//     white1 += cans[arr1[i]][0];
//     black1 += cans[arr1[i]][1];
//   }
//   for (let i = 0; i < arr1.length; i++) {
//     cans.splice(arr1[i], 1);
//   }
//   for (const blackCount of cans) {
//     white2 += blackCount[0];
//     black2 += blackCount[1];
//   }
//   return Math.min(Math.abs(black1 - white2), Math.abs(black2 - white1));
// };

// function solution(cans) {
//   let answer = Infinity;
//   const comb = arr => {
//     if (arr.length === cans.length / 2) {
//       answer = Math.min(answer, score(arr, cans.slice()));
//       return;
//     }
//     for (let i = 0; i < cans.length; i++) {
//       if (arr.includes(i)) continue;
//       const newArr = arr.slice();
//       newArr.push(i);
//       comb(newArr);
//     }
//   };
//   comb([]);
//   return answer;
// }
// // 조합으로 선수 조합

// // 점수 구하는 함수

// console.log(solution([[87, 84], [66, 78], [94, 94], [93, 87], [72, 92], [78, 63]]));

// const solution1 = cans => {
//   let answer = Number.MAX_SAFE_INTEGER;
//   const len = cans.length;
//   const ch = Array.from({ length: len }, () => 0);
//   const dfs = (lev, s) => {
//     if (lev === len / 2) {
//       const A = []; const
//         B = [];
//       for (let i = 0; i < len; i++) {
//         if (ch[i] === 1) A.push(i);
//         else B.push(i);
//       }
//       let Asum = 0; let
//         Bsum = 0;
//       for (let i = 0; i < A.length; i++) {
//         Asum += cans[A[i]][0];
//         Bsum += cans[B[i]][1];
//       }
//       answer = Math.min(answer, Math.abs(Asum - Bsum));
//     } else {
//       for (let i = s; i < len; i++) {
//         ch[i] = 1;
//         dfs(lev + 1, i + 1);
//         ch[i] = 0;
//       }
//     }
//   };
//   dfs(0, 0);
// };
// console.log(solution1([[87, 84], [66, 78], [94, 94], [93, 87], [72, 92], [78, 63]]));

const solution2 = (c, r, arr) => {
  const ch = Array.from({ length: c }, () => 0);
  const answer = []; const temp = [];

  const dfs = (lev, s) => {
    if (lev === r) {
      answer.push(temp.slice());
    } else {
      for (let i = s; i < c; i++) {
        temp.push(arr[i]);
        dfs(lev + 1, i + 1);
        temp.pop();
      }
    }
  };
  dfs(0, 0);
  return answer;
};
console.log(solution2(5, 3, [2, 7, 9, 8, 5]));
