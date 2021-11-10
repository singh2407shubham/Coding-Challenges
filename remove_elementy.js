let arr = [2,1,3,2,5];
let k = 2;

const removeElement = function(nums, val) {
  let shiftedElements = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != val) {
      nums[shiftedElements] = nums[i];
      shiftedElements++;
    }
  }
  return shiftedElements;
}

console.log(removeElement(arr, k));
console.log(arr);
