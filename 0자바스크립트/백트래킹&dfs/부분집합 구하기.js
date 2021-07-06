const solution = K => {
  const recur = (K, arr) => {
    if (K === arr.length) return arr;
    for (let i = 1; i < K + 1; i++) {
      if (!arr.includes(i)) arr.push(i);

      console.log(recur(i, arr));
    }
  };
  const answer = recur(K, []);
};
solution(3);
