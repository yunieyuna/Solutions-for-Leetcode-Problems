/*  
Question Link: https://leetcode.com/problems/maximum-subarray/
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    // DP
    let local_max = 0;
    let global_max = Number.NEGATIVE_INFINITY;

    for (let i = 0; i < nums.length; i++) {
        local_max = Math.max(nums[i], nums[i] + local_max)

        if (local_max > global_max) {
            global_max = local_max
        }
    }

    return global_max
};
