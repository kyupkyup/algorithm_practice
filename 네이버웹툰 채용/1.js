function solution(k, rates) {
  const answer = 0;
  let state = 'low';
  let currentPointer = 0;
  let buy = 0;
  let currentMoney = k;
  while (currentPointer < rates.length) {
    if (state === 'low') {
      if (currentMoney < rates[currentPointer]) {
        currentPointer += 1;
        continue;
      } else {
        if (currentPointer + 1 >= rates.length) break;
        while (rates[currentPointer] > rates[currentPointer + 1]) {
          currentPointer += 1;
        }
        state = 'high';
        buy = rates[currentPointer];
      }
    }
    if (state === 'high') {
      if (currentPointer + 1 >= rates.length) break;

      while (rates[currentPointer] < rates[currentPointer + 1]) {
        currentPointer += 1;
      }
      state = 'low';
      currentMoney += rates[currentPointer] - buy;
    }
  }
  return currentMoney;
}

console.log(solution(1000, [1500, 500, 1000, 500, 1500]));
