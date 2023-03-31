class Solution {
    public void rotate(int[] nums, int k) {
        int[] numsC = new int[nums.length];
        k %= nums.length;
        for (int i = k; i < numsC.length; i++)
            numsC[i] = nums[i-k];
        for (int i = 1, j = k-1; i <= k; i++, j--) 
            numsC[j] = nums[nums.length - i];
        for (int i = 0; i < numsC.length; i++)
            nums[i] = numsC[i];
    }
}