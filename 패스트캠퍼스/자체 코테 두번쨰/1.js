function solution(s, e) {
  let answer = 0;
  let hyun = s;

  while (hyun !== e) {
    if (e - hyun > 2) {
      hyun += 5;
      answer += 1;
      continue;
    } else if (hyun > e) {
      hyun -= 1;
      answer += 1;
      continue;
    } else if (hyun < e) {
      hyun += 1;
      answer += 1;
      continue;
    }
  }
  return answer;
}

console.log(solution(5, 14));

//   const visited = new Set();
//   visited.add(s);
//   const dq = [];
//   dq.push([s, 0]);

//   while (dq) {
//     const [start, count] = dq.shift();
//     if (start === e) {
//       return count;
//     }
//     if (!visited.has(start - 1)) dq.push([start - 1, count + 1]);
//     if (!visited.has(start + 1))dq.push([start + 1, count + 1]);
//     if (!visited.has(start + 5))dq.push([start + 5, count + 1]);
//   }
