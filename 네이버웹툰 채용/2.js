function solution(money, cost) {
  const func = (money, cost) => {
    let currentMoney = money;
    const dp = [];
    for (let i = 0; i < cost.length; i++) {
      dp.push(0);
    }

    for (let i = 0; i < cost.length; i++) {
      if (cost[i] <= currentMoney) {
        if (i === 0) {
          dp[i] += 1;
        } else {
          dp[i] += dp[i - 1] + 1;
        }
        currentMoney -= cost[i];
      } else {
        dp[i] = 0;
        currentMoney = money;
      }
    }

    return Math.max(...dp);
  };
  return Math.max(func(money, cost), func(money, cost.reverse()));
}

console.log(solution(100, [245, 317, 151, 192]));
