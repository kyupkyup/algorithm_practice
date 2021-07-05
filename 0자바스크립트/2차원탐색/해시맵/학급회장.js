const solution = (N, votes) => {
  const answer = new Map();
  for (const vote of votes) {
    if (answer.has(vote)) answer.set(vote, answer.get(vote) + 1);
    else answer.set(vote, 1);
  }
  return [...answer].sort((a, b) => (b[1] - a[1]))[0][0];
};

console.log(solution(15, 'BACBACCACCBDEDE'));
