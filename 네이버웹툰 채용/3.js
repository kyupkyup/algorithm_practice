function solution(block, board) {
  let answer = 0;
  const obj = {
    0: [[0, 0], [0, 1], [0, 2], 1],
    1: [[0, 0], [1, 0], [2, 0], 3],
    2: [[0, 0], [0, 1], [1, 1], 2],
    3: [[1, 0], [0, 1], [1, 1], 2],
    4: [[0, 0], [1, 0], [1, 1], 2],
    5: [[0, 0], [1, 0], [0, 1], 2],
  };

  for (let j = 0; j < board.length; j++) {
    for (let i = 0; i < board.length; i++) {
      const newBoard = [];
      for (let z = 0; z < board.length; z++) {
        const temp = board[z].slice();
        newBoard.push(temp);
      }

      for (let k = 0; k < 3; k++) {
        if (j + obj[block][k][1] >= 0 && j + obj[block][k][1] < board.length && i + obj[block][k][0] >= 0
            && i + obj[block][k][0] < board.length) {
          newBoard[j + obj[block][k][1]][i + obj[block][k][0]] += 1;
        }
      }
      // 2있나 검증 코드
      let twoCheck = false;
      for (let n = 0; n < board.length; n++) {
        for (let m = 0; m < board.length; m++) {
          if (newBoard[n][m] === 2) {
            twoCheck = true;
            break;
          }
        }
        if (twoCheck) break;
      }
      if (twoCheck) continue;
      // 공중에 떠있나 체크
      let blowCheck = 0;
      for (let k = 0; k < 3; k++) {
        if (j + obj[block][k][1] < board.length - 1) {
          if (newBoard[j + obj[block][k][1] + 1][i + obj[block][k][0]] === 0) blowCheck += 1;
        }
        if (blowCheck === obj[block][3]) break;
      }
      if (blowCheck === obj[block][3]) continue;
      // 없어지는 줄 수 체크

      let count = 0;
      let realCount = 0;
      for (let a = 0; a < board.length; a++) {
        for (let b = 0; b < board.length; b++) {
          if (newBoard[a][b] === 1) count += 1;
        }
        if (count === board.length) {
          realCount += 1;
        }
        count = 0;
        answer = Math.max(answer, realCount);
      }
    }
  }
  console.log(answer);
  return answer;
}

solution(5, [[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]);
