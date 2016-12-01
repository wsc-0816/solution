public class Solution {
    public int threeSumClosest(int[] nums, int target) {
       if (nums == null || nums.length< 3){
           return -1;
       }
       Arrays.sort(nums);
       int result = nums[0]+nums[1] + nums[2];
       for (int i = 0; i<nums.length;i++){
           int s = i + 1;
           int e = nums.length - 1;
           while (s < e){
               int temp = nums[i]+nums[s]+nums[e];
               if (Math.abs(target - temp) < Math.abs(target-result)){
                   result = temp;
               }
               if (temp < target){
                   s++;
               }
               else{
                   e--;
               }
           }
       }
       return result;
    }
}