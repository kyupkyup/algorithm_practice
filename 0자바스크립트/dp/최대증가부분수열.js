const solution = arr => {
  const dp = [];
  const parent = [];
  for (let i = 0; i < arr.length; i++) {
    dp.push(1);
  }
  for (let i = 0; i < arr.length; i++) {
    parent.push(-1);
  }
  for (let i = 0; i < arr.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      if (arr[i] > arr[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }
  console.log(parent);

  const print = n => {

  };
  console.log(dp);
};
solution([5, 3, 7, 8, 6, 2, 9, 4]);
