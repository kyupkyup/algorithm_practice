function solution(times) {
  const answer = 0;
  const arr = Array.from({ length: 100000 }, () => 0);
  for (let i = 0; i < times.length; i++) {
    for (let j = times[i][0]; j < times[i][1]; j++) {
      arr[j] += 1;
    }
  }

  return Math.max(...arr);
}

console.log(solution([[14, 18], [12, 15], [15, 20], [20, 30], [5, 14]]));
