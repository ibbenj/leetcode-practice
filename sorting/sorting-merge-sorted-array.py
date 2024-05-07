class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while len(nums1) > m:
            nums1.pop()

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                j+=1
                m+=1
            else:
                i+=1

        while j < n:
            nums1.append(nums2[j])
            j+=1           



        """
        Do not return anything, modify nums1 in-place instead.
        """
        