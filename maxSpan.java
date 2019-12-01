/*

Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)


maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
*/

public int maxSpan(int[] nums) {
  int span = 1;
  int maxSpan = 0;
  int curr = 0;
  int i = 0;
  while(i<nums.length){
    curr = nums[i];
    span = 1;
    for(int j=i+1;j<nums.length;j++){
      if(curr==nums[j]){
        span = j-i+1;
      }
    }
    if(maxSpan<span){
      maxSpan = span;
    }
    i++;
  }
  return maxSpan;
}