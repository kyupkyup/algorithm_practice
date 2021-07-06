// const isNumber = val => Number(val) === val;

// const copy = (s, num) => {
//   let pointer = 0;
//   let str = '';

//   while (pointer < s.length) {
//     let number = 0;

//     if (isNumber(+s[pointer])) {
//       let temp = s[pointer];
//       if (isNumber(+s[pointer + 1])) {
//         temp = s[pointer] + s[pointer + 1];
//         pointer += 1;
//       }

//       number = +temp;
//       pointer += 2;
//       const [returnStr, returnPointer] = copy(s.slice(pointer, s.length), number);
//       str += returnStr;
//       pointer += returnPointer;
//     } else if (s[pointer] === ')') {
//       let newStr = '';
//       for (let i = 0; i < num; i++) newStr += str;
//       return [newStr, pointer];
//     } else {
//       str += s[pointer];
//     }
//     pointer += 1;
//   }
//   return str;
// };
// function solution(s) {
//   return copy(s);
// }
const isNumber = val => Number(val) === val;

const solution = S => {
  const stack = [];
  const pointer = 0;
  while (pointer < S.length) {
    if (pointer !== '(') {
      stack.push(S[pointer]);
    } else {

    }
  }
};

console.log(solution('3(a2(b))ef'));
