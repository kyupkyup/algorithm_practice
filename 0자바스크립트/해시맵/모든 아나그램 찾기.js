const solution = (str1, str2) => {
  let answer = 0;
  let newStr = str1.slice(0, str2.length);
  const check = str1 => {
    const map = new Map();
    for (let i = 0; i < str1.length; i++) {
      if (map.has(str1[i])) map.set(str1[i], map.get(str1[i]) + 1);
      else map.set(str1[i], 1);
    }
    for (let i = 0; i < str2.length; i++) {
      if (map.has(str2[i])) {
        map.set(str2[i], map.get(str2[i]) - 1);
        if (map.get(str2[i]) < 0) {
          return false;
        }
      } else return false;
    }
    return true;
  };
  for (let i = str2.length; i < str1.length; i++) {
    if (check(newStr)) answer += 1;
    newStr = newStr.slice(1, newStr.length) + str1[i];
  }
  if (check(newStr)) answer += 1;

  return answer;
};

console.log(solution('bacaAacba', 'abc'));

const [answer, min_odd] = [[], []];
console.log(answer);
console.log(min_odd);
