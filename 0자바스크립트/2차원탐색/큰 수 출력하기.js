const solution = (N, arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    if (i === 0) {
      console.log(arr[i]);
    } else if (arr[i] < arr[i + 1]) {
      console.log(arr[i + 1]);
    }
  }
};

solution(6, [7, 3, 9, 5, 6, 12]);
