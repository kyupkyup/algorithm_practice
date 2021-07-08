const solution = K => {
  const check = [];
  for (let i = 0; i < K; i++) {
    check.push(false);
  }
  const recur = n => {
    if (n === K) {
      let tmp = '';
      for (let i = 0; i < K; i++) {
        if (check[i]) tmp += i + 1 + ' ';
      }
      console.log(tmp);
    } else {
      check[n] = true;
      recur(n + 1);
      check[n] = false;
      recur(n + 1);
    }
  };
  recur(0);
};
solution(3);
