function solution(n, f) {
  let answer = [];
  const check = [];
  let finished = false;
  for (let i = 0; i < n + 1; i++) {
    check.push(false);
  }

  const checkFunc = arr => {
    const newArr = [];
    if (arr.length === 1) return arr[0];
    for (let i = 1; i < arr.length; i++) {
      newArr.push(arr[i] + arr[i - 1]);
    }
    return checkFunc(newArr);
  };

  const recur = arr => {
    if (arr.length === n) {
      const number = checkFunc(arr);
      if (number === f) {
        finished = true;
        answer = arr;
        return;
      }
      return;
    }

    for (let i = 1; i < n + 1; i++) {
      if (!check[i]) {
        check[i] = true;
        const newArr = arr.slice();
        newArr.push(i);
        recur(newArr);
        if (finished) return;
        check[i] = false;
        newArr.pop();
      }
    }
  };
  recur([]);
  return answer;
}

console.log(solution(4, 16));
