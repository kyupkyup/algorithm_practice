const factorial = num => {
  let result = 1;
  for (let i = num; i > 0; i--) {
    result *= i;
  }
  return result;
};

const sliceNum = n => {
  let result = 0;
  for (let i = 0; i < n.length; i++) {
    result += factorial(+n[i]);
  }
  return result;
};

function solution(n) {
  // Write your code here
  let result = n;
  const answer = new Set();
  answer.add(n);
  while (true) {
    const preAnswerSize = answer.size;
    result = sliceNum('' + result);
    answer.add(result);
    if (answer.size === preAnswerSize) {
      break;
    }
  }
  return Math.max(...answer) * answer.size;
}

console.log(solution(4));
