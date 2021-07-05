function solution(board) {
  const dx = [0, 0, -1, 1];
  const dy = [1, -1, 0, 0];
  let answer = Number.MAX_VALUE;

  const bfs = board => {
    let count = 0;
    const dq = [];
    const visited = [];
    for (let j = 0; j < board.length; j++) {
      const temp = [];
      for (let i = 0; i < board.length; i++) {
        temp.push(false);
      }
      visited.push(temp);
    }
    for (let j = 0; j < board.length; j++) {
      for (let i = 0; i < board.length; i++) {
        if (board[j][i] === 1 && !visited[j][i]) {
          dq.push([i, j]);
          visited[j][i] = true;
          count += 1;
        }
        while (dq.length > 0) {
          const [x, y] = dq.shift();
          for (let k = 0; k < 4; k++) {
            const nx = x + dx[k];
            const ny = y + dy[k];
            if (nx >= 0 && nx < board.length && ny >= 0 && ny < board.length) {
              if (!visited[ny][nx] && board[ny][nx] === 1) {
                visited[ny][nx] = true;
                dq.push([nx, ny]);
              }
            }
          }
        }
      }
    }
    if (count > 1) return false;
    return true;
  };

  const dfs = (i, j, count, board) => {
    const newBoard = [];
    for (let m = 0; m < board.length; m++) {
      newBoard.push(board[m].slice());
    }
    newBoard[j][i] = 1;

    if (bfs(newBoard)) {
      answer = Math.min(answer, count);
      return;
    }
    for (let k = 0; k < 4; k++) {
      const nx = i + dx[k];
      const ny = j + dy[k];
      if (nx >= 0 && nx < board.length && ny >= 0 && ny < board.length) {
        if (newBoard[ny][nx] === 0) {
          dfs(nx, ny, count + 1, newBoard);
        }
      }
    }
  };

  const count = 0;
  for (let j = 0; j < board.length; j++) {
    for (let i = 0; i < board.length; i++) {
      if (board[j][i] === 0) {
        dfs(i, j, count + 1, board);
      }
    }
  }

  return answer;
}

console.log(solution([[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1]]));
