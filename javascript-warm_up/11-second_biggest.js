#!/usr/bin/node
function findSecondBiggest (nums) {
  if (nums.length < 2) {
    return 0;
  }
  nums.sort((a, b) => b - a);
  return nums[1];
}

if (process.argv.length > 2) {
  const numbers = process.argv.slice(2).map(n => parseInt(n, 10));
  const result = findSecondBiggest(numbers);

  console.log(result);
} else {
  console.log(0);
}
