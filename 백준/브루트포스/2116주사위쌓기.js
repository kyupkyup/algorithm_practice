const solution = (M, squareList) => {
  const index = [[0, 5], [1, 3], [2, 4], [5, 0], [4, 2], [3, 1]];
  let rAnswer = 0;
  const findMax = (floorIdx, ceilIdx, j) => {
    const temp = squareList[j].filter((_, idx) => (idx !== floorIdx && idx !== ceilIdx));
    return Math.max(...temp);
  };
  const recur = (idx, j, answer) => {
    if (j === M - 1) {
      return answer;
    }
    // 바닥 값을 받으면 해당 인덱스를 찾아서
    // const valueIndex = squareList[j].indexOf(value);
    const ceilIndex = index.filter(item => item[0] === idx)[0][1];
    const nextValue = squareList[j][ceilIndex];
    const nextFloorIndex = squareList[j + 1].indexOf(nextValue);
    const max = findMax(idx, ceilIndex, j);
    return recur(nextFloorIndex, j + 1, answer + max);
    // 다시 인덱스
  };
  // 마주보는 인덱스 [0,5] [1,3] [2,4]
  // 맨밑의 경우의 수
  for (let i = 0; i < 6; i++) {
    // 해당 인덱스를 바닥에 둘 경우, 다음 인덱스의 값을 다음 주사위에서 구해서 해당 인덱스를 바닥으로 함.
    // const next = index.filter(item => item[0] === i);

    rAnswer = Math.max(rAnswer, recur(i, 0, 0));
  }
  // 윗면도 결정
  // 4개 면 중 가장 큰 것 선택
  console.log(rAnswer);
};
const fs = require('fs');

const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
  `
).split('\n');

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const M = parseInt(input(), 10);
const squareList = [];
let flag = M;
while (flag--) {
  const square = input().split(' ').map(Number);
  squareList.push(square);
}
solution(M, squareList);
