Set.prototype.isSuperset = function (subset) {
  for (const value of subset) {
    if (!this.has(value)) return false;
  }
  return true;
};
function solution(nums, d, k) {
  let answer = Number.MIN_SAFE_INTEGER;
  const check = [];
  for (let i = 0; i < d + 1; i++) {
    check.push(false);
  }
  const setIngre = new Set();
  const checkSet = set => {
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
      console.log(new Set(nums[i]));
      if (set.isSuperset(new Set(nums[i]))) count += 1;
    }
    return count;
  };
  const recur = (set, lev) => {
    if (lev === k) {
      answer = Math.max(answer, checkSet(set));
      return;
    }
    for (let i = 1; i < d + 1; i++) {
      if (!check[i]) {
        check[i] = true;
        set.add(i);
        recur(set, lev + 1);
        check[i] = false;
        set.delete(i);
      }
    }
  };
  recur(setIngre, 0);
  return answer;
}

console.log(solution([[1], [2, 3], [3], [1, 2], [], [2, 1], [2, 3, 4], [3, 4]], 4, 3));
