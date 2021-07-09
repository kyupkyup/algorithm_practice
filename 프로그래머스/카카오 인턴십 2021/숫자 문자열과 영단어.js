const isNumber = val => Number(val) === val;

function solution(s) {
  let answer = '';
  let temp = '';
  for (let i = 0; i < s.length; i++) {
    if (isNumber(+s[i])) {
      answer += s[i];
      continue;
    }
    temp += s[i];
    if (temp === 'zero') {
      answer += '0';
      temp = '';
    }
    if (temp === 'one') {
      answer += '1';
      temp = '';
    }
    if (temp === 'two') {
      answer += '2';
      temp = '';
    }
    if (temp === 'three') {
      answer += '3';
      temp = '';
    }
    if (temp === 'four') {
      answer += '4';
      temp = '';
    }
    if (temp === 'five') {
      answer += '5';
      temp = '';
    }
    if (temp === 'six') {
      answer += '6';
      temp = '';
    }
    if (temp === 'seven') {
      answer += '7';
      temp = '';
    }
    if (temp === 'eight') {
      answer += '8';
      temp = '';
    }
    if (temp === 'nine') {
      answer += '9';
      temp = '';
    }
  }

  return +answer;
}
console.log(solution('one4seveneight'));
