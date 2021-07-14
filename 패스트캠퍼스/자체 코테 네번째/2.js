Set.prototype.intersection = function (set) {
  const result = new Set();
  for (const value of set) {
    if (this.has(value)) result.add(value);
  }
  return result;
};

function solution(A, B, C) {
  const setA = new Set(A);
  const setB = new Set(B);
  const setC = new Set(C);
  const AB = setA.intersection(setB);
  const ABC = AB.intersection(setC);
  return Math.max(...ABC);
}
console.log(solution([39, 31, 32, 75, 73, 7, 89, 21, 7, 67], [4, 19, 52, 75, 35, 100, 4, 26, 24, 69], [82, 53, 22, 64, 58, 80, 94, 75, 51, 69]));
