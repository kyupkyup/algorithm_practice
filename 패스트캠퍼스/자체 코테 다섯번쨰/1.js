const solution = (n, k) => {
  const arr = [];
  for (let j = 0; j < n; j++) {
    const temp = [];
    for (let i = 0; i < n; i++) {
      temp.push(0);
    }
    arr.push(temp);
  }
  let x = 0; let y = -1; let
    s = 1;
  let cnt = 1;
  while (true) {
    for (let i = 0; i < n; i++) {
      y += s;
      if (cnt === k) return [y, x];
      arr[x][y] = cnt++;
    }
    n--;
    if (n === 0) break;
    for (let i = 0; i < n; i++) {
      x += s;
      if (cnt === k) return [y, x];
      arr[x][y] = cnt++;
    }

    s *= -1;
  }
  console.log(arr);
};
console.log(solution(5, 15));
