const solution = (N, arr) => {
  let max = -1;
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (max < arr[i]) {
      count += 1;
      max = arr[i];
    }
  }
  console.log(count);
};

solution(8, [130, 135, 148, 140, 145, 150, 150, 153]);
