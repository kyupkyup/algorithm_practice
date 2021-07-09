function solution(places) {
  const answer = [];
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, -1, 1];
  for (let i = 0; i < places.length; i++) {
    answer.push(-1);
  }
  for (let place = 0; place < place.length; place++) {
    // bfs 2단계까지
    const visited = [];
    const dq = [];
    for (let i = 0; i < place.length; i++) {
      const temp = [];
      for (let j = 0; j < place.length; j++) {
        if (place[j][i] === 'P') {
          dq.push([i, j, 0]);
        }
        temp.push(false);
      }
      visited.push(temp);
    }

    while (dq.length > 0) {
      const [x, y, lev] = dq.shift();
      if (lev >= 2) continue;
      if (place[y][x] === 'P') {
        answer[place] = 0;
        break;
      } else if (place[y][x] === 'X') {
        continue;
      }
      for (let k = 0; k < 4; k++) {
        const nx = x + dx[k];
        const ny = y + dy[k];
        if (nx >= 0 && nx < place.length && ny >= 0 && ny < places.length) {

        }
      }
    }
  }

  return answer;
}
console.log(solution([['POOOP', 'OXXOX', 'OPXPX', 'OOXOX', 'POXXP'], ['POOPX', 'OXPXP', 'PXXXO', 'OXXXO', 'OOOPP'], ['PXOPX', 'OXOXP', 'OXPOX', 'OXXOP', 'PXPOX'], ['OOOXX', 'XOOOX', 'OOOXX', 'OXOOX', 'OOOOO'], ['PXPXP', 'XPXPX', 'PXPXP', 'XPXPX', 'PXPXP']]));
