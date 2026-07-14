class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            # make nums1 always be the smaller of the two
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) -1
        while True:
            i = (l + r) // 2  # nums1
            j = half - i - 2  # nums2  -2 since half includes two array lengths both indexed at 0

            nums1left = nums1[i] if i >= 0 else float("-infinity")
            nums1right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
            nums2left = nums2[j] if j >= 0 else float("-infinity")
            nums2right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")

            if nums1left <= nums2right and nums2left <= nums1right:
                # odd
                if total % 2:
                    return min(nums1right, nums2right)
                # even
                return (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2
            elif nums1left > nums2right:
                r = i - 1
            else:
                l = i + 1
