class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] smallerNum = new int[101];
        
        for(int i = 0; i < nums.length; i++){
            smallerNum[nums[i]]++;
        }
        
        for(int i = 1; i < 101; i++){
            smallerNum[i] += smallerNum[i-1];
        }
        
        for(int i = 0; i<nums.length; i++){
            int index = nums[i];
            if(index == 0){
                nums[i] = 0;
            }
            else
                nums[i] = smallerNum[index - 1];
        } 
         return nums;
    }
   
}