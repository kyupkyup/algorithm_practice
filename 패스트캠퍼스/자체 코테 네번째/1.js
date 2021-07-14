function solution(strs) {
  let answer = '';
  let pointer = 0;

  while (true) {
    const temp = new Set();
    for (let i = 0; i < strs.length; i++) {
      if (strs[i].length < pointer) return answer;
      temp.add(strs[i][pointer]);
    }
    if (temp.size !== 1) return answer;
    if (temp.size === 1) answer += strs[0][pointer];
    pointer += 1;
  }
}
console.log(solution(['long', 'longtime', 'longest']));
