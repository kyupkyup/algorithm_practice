function solution(board) {
  const dx = [0, 0, -1, 1];
  const dy = [1, -1, 0, 0];
  const dq = [];
  const visited = [];
  let answer = Number.MAX_SAFE_INTEGER;
  for (let j = 0; j < board.length; j++) {
    const temp = [];
    for (let i = 0; i < board.length; i++) {
      temp.push(false);
    }
    visited.push(temp);
  }

  const dfs = (i, j) => {
    if (board[j][i] === 0) {
      return;
    }

    for (let k = 0; k < 4; k++) {
      const nx = i + dx[k];
      const ny = j + dy[k];
      if (nx >= 0 && nx < board.length && ny >= 0 && ny < board.length) {
        if (!visited[ny][nx] && board[ny][nx] === 1) {
          visited[ny][nx] = true;
          dq.push([[nx, ny], 0]);
          dfs(nx, ny);
        }
      }
    }
  };
  let flag = false;
  for (let j = 0; j < board.length; j++) {
    for (let i = 0; i < board.length; i++) {
      if (board[j][i] === 1) {
        visited[j][i] = true;
        dq.push([[i, j], 0]);
        dfs(i, j);
        flag = true;
        break;
      }
    }
    if (flag) break;
  }

  while (dq.length > 0) {
    const [[x, y], count] = dq.shift();
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (nx >= 0 && nx < board.length && ny >= 0 && ny < board.length) {
        if (!visited[ny][nx] && board[ny][nx] === 0) {
          visited[ny][nx] = true;
          dq.push([[nx, ny], count + 1]);
        } else if (!visited[ny][nx] && board[ny][nx] === 1) {
          answer = Math.min(answer, count);
        }
      }
    }
  }
  return answer;
}

console.log(solution([[1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1]]));
