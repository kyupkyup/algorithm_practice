const score = (arr1, cans) => {
  let white1 = 0;
  let black1 = 0;
  let white2 = 0;
  let black2 = 0;
  arr1.sort((a, b) => b - a);
  for (let i = 0; i < arr1.length; i++) {
    white1 += cans[arr1[i]][0];
    black1 += cans[arr1[i]][1];
  }
  for (let i = 0; i < arr1.length; i++) {
    cans.splice(arr1[i], 1);
  }
  for (const blackCount of cans) {
    white2 += blackCount[0];
    black2 += blackCount[1];
  }
  //   console.log(arr1);
  //   console.log(cans);

  //   console.log(arr1);
  //   console.log(white1);
  //   console.log(black1);
  //   console.log(white2);
  //   console.log(black2);
  return Math.min(Math.abs(black1 - white2), Math.abs(black2 - white1));
};

function solution(cans) {
  let answer = Infinity;
  const comb = arr => {
    if (arr.length === cans.length / 2) {
      answer = Math.min(answer, score(arr, cans.slice()));
      return;
    }
    for (let i = 0; i < cans.length; i++) {
      if (arr.includes(i)) continue;
      const newArr = arr.slice();
      newArr.push(i);
      comb(newArr);
    }
  };
  comb([]);
  return answer;
}
// 조합으로 선수 조합

// 점수 구하는 함수

console.log(solution([[87, 84], [66, 78], [94, 94], [93, 87], [72, 92], [78, 63]]));
