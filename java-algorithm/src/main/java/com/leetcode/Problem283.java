package com.leetcode;

/**
 * 283. Move Zeroes
 * https://leetcode.com/problems/move-zeroes/
 *
 * Given an array nums, write a function to move all 0's to the end of it
 * while maintaining the relative order of the non-zero elements.
 *
 * Example:
 *
 * Input: [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 *
 * Note:
 *
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.
 */
public class Problem283 {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) continue;
            int j = i + 1;
            while (j < n && nums[j] == 0) j++;
            if (j < n) {
                nums[i] = nums[j];
                nums[j] = 0;
            }
        }
    }
}
