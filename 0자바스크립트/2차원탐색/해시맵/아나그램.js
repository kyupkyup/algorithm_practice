const solution = (s1, s2) => {
  const map = new Map();
  for (const word of s1) {
    if (map.has(word)) map.set(word, map.get(word) + 1);
    else map.set(word, 1);
  }
  for (const word of s2) {
    if (map.has(word)) map.set(word, map.get(word) - 1);
    else return 'NO';
  }
  let flag = false;
  map.forEach(item => {
    if (item !== 0) flag = true;
  });
  if (flag) return 'NO';
  return 'YES';
};

console.log(solution('AbaAeCe', 'baeeACA'));
