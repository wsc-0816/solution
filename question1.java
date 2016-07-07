import java.util.*;

public class question1 {
   public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i= 0;i < nums.length;i++){
            int temp1 = nums[i];
            int differ = target - temp1; 
            for (int j = 0;j < nums.length;j++){
                if (nums[j] == differ){
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
    return result;}


 public static void main(String[] args){
    int[] test =  { 4, 6, 3, 4, 6 };
    int target =  20;
    System.out.println("sdf");
    question1 t = new question1();
    int[] result = t.twoSum(test,target);
    System.out.println("[" + result[0] +" ," +result[1] + "]");
 }
}