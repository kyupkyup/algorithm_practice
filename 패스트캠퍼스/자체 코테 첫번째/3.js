function solution(nums, m) {
  const answer = [];
  const overlay = new Set();
  const minus = (m, arr) => {
    if (m === 0) {
      answer.push(arr);
      return;
    }

    for (const number of nums) {
      if (m - number < 0) continue;
      const newArr = arr.slice();
      newArr.push(number);
      minus(m - number, newArr);
    }
  };
  minus(m, []);

  for (const array of answer) {
    const newStr = array.sort().join('');
    overlay.add(newStr);
  }

  return overlay.size;
}

console.log(solution([2, 3, 5], 10));
