function solution(height) {
  const answer = [];

  const stack = [];

  for (let i = 0; i < height.length; i++) {
    if (stack.length === 0) {
      stack.push([height[i], i + 1]);
      answer.push(0);
    } else {
      while (stack.length !== 0 && stack[stack.length - 1][0] <= height[i]) {
        stack.pop();
      }
      if (stack.length === 0) {
        stack.push([height[i], i + 1]);
        answer.push(0);
      } else {
        answer.push(stack[stack.length - 1][1]);
        stack.push([height[i], i + 1]);
      }
    }
  }

  return answer;
}

console.log(solution([50, 57, 52, 53, 51]));
