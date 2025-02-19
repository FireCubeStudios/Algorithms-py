class Solution:
    # If nums[i] = x, then y = target - x where y = nums[ii]
    # We add array items to hashmap in O(n) linear time
    # The hashmap will have key = nums[i] and value = i, aka <nums[i], i>
    # We look up in hashmap for key which solves y = target - x in O(1) constant time
    # Loop through all nums elements until solution found, this takes O(n) linear time
    # We ignore item at same index with i != ii and also if no solution found for that i
    # The runtime is linear O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            ii = hashmap.get(target - nums[i])
            if ii != None and i != ii:
                return [i, ii]


    # Brute force solution O(n^2)
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for ii in range(len(nums)):
                if i == ii: 
                    continue # Ignore number at same index
                if nums[i] + nums[ii] == target:
                    return [i, ii]