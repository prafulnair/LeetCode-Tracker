class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        if n == 0:
            return
        
        p = m - 1  
        q = n - 1
        k = len(nums1) - 1

        while p >= 0 and q >= 0:
            if nums2[q] > nums1[p]:
                nums1[k] = nums2[q]
                k -= 1
                q -= 1
            else:
                nums1[k] = nums1[p]
                k -= 1
                p -= 1

        # If there are remaining elements in nums2, copy them
        while q >= 0:
            nums1[k] = nums2[q]
            k -= 1
            q -= 1

        return nums1


"""

we know there would be  0s in the end of nums1
so we start merging at the end
k points to the last 0, which we will use as the place where we can add the largest of the two elements from nums1 and nums2
pointers for nums1 and nums2 - p and q respectively, points to its last element (non-zero element for nums1)

we simply compare the last two numbers of both array, and place the larger one at kth index of nums1, 
then we decrement k and the 
pointer who's number was bigger

also in the end we check if there is any remaining element in nums 2 and put all that in nums 1 

"""