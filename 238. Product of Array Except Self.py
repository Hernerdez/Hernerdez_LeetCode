# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# Topic: Array, Prefix Sum

"""
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

Key Constraints:
- Cannot use division operation
- Must run in O(n) time
- Follow up: O(1) extra space (output array doesn't count)
"""

from typing import List

# ============================================================================
# Approach 1: Brute Force (Time Limit Exceeded on LeetCode)
# Time: O(n²) - nested loops
# Space: O(1) - only output array
# ============================================================================
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        # For each position i
        for i in range(n):
            product = 1
            # Multiply all elements except nums[i]
            for j in range(n):
                if i != j:
                    product *= nums[j]
            result.append(product)

        return result

# ============================================================================
# Approach 2: Using Left and Right Product Arrays
# Time: O(n) - three passes through the array
# Space: O(n) - two extra arrays for left and right products
# ============================================================================
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build array of products to the left of each element
        # left_products[i] = product of all elements before index i
        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]

        # Build array of products to the right of each element
        # right_products[i] = product of all elements after index i
        right_products = [1] * n
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        # For each position, multiply left and right products
        result = []
        for i in range(n):
            result.append(left_products[i] * right_products[i])

        return result

# ============================================================================
# Approach 3: Optimized O(1) Space Solution (Best)
# Time: O(n) - two passes through the array
# Space: O(1) - output array doesn't count as extra space
# ============================================================================
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # First pass: Calculate left products and store in result
        # result[i] will contain product of all elements to the left of i
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]

        # Second pass: Multiply by right products on the fly
        # We use a variable to track the running product from the right
        right_product = 1
        for i in range(n-1, -1, -1):
            # result[i] already has left product, multiply by right product
            result[i] *= right_product
            # Update right product for next iteration
            right_product *= nums[i]

        return result

# ============================================================================
# Example Walkthrough with nums = [1,2,3,4]
# ============================================================================
"""
Step-by-step trace of optimized solution:

Initial: nums = [1,2,3,4]

Pass 1 - Building left products in result:
i=0: result = [1, 1, 1, 1] (base case, nothing to left of index 0)
i=1: result[1] = result[0] * nums[0] = 1 * 1 = 1
     result = [1, 1, 1, 1]
i=2: result[2] = result[1] * nums[1] = 1 * 2 = 2
     result = [1, 1, 2, 1]
i=3: result[3] = result[2] * nums[2] = 2 * 3 = 6
     result = [1, 1, 2, 6]

Pass 2 - Multiplying by right products:
right_product = 1
i=3: result[3] = 6 * 1 = 6, right_product = 1 * 4 = 4
     result = [1, 1, 2, 6]
i=2: result[2] = 2 * 4 = 8, right_product = 4 * 3 = 12
     result = [1, 1, 8, 6]
i=1: result[1] = 1 * 12 = 12, right_product = 12 * 2 = 24
     result = [1, 12, 8, 6]
i=0: result[0] = 1 * 24 = 24, right_product = 24 * 1 = 24
     result = [24, 12, 8, 6]

Output: [24, 12, 8, 6] ✓
"""

# ============================================================================
# Test Cases
# ============================================================================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        ([2,3,4,5], [60,40,30,24]),
        ([1,0], [0,1]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.productExceptSelf(nums)
        print(f"Test {i}:")
        print(f"  Input: {nums}")
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        print(f"  Pass: {result == expected}\n")