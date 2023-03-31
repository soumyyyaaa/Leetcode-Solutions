class Solution {
    public int[] sortedSquares(int[] nums) {
        int numsS[] = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numsS[i] = nums[i] * nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (numsS[i] > numsS[j]) {
                    int c = numsS[i];
                    numsS[i] = numsS[j];
                    numsS[j] = c;
                }
            }
        }
        return numsS;
    }
}