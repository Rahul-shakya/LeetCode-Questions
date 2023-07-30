class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProd = [0] * len(nums)
        suffProd = [0] * len(nums)
        prefProd[0] = nums[0]
        suffProd[len(nums) - 1] = nums[len(nums) - 1]
        ans = []

        for i in range(1, len(nums)):
            prefProd[i] = nums[i] * prefProd[i-1]

        for i in range(len(nums) - 2, -1, -1):
            suffProd[i] = suffProd[i+1] * nums[i]
        
        ans.append(suffProd[1])
        for i in range(1, len(nums) - 1):
           ans.append(prefProd[i-1] * suffProd[i+1])
        ans.append(prefProd[len(nums) - 2])

        return ans

    # better way
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n # initialize left_product array with 1
        right_product = [1] * n # initialize right_product array with 1
        # calculate the product of elements to the left of each element
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        # calculate the product of elements to the right of each element
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # calculate the product of all elements except nums[i]
        result = [left_product[i] * right_product[i] for i in range(n)]

        return result