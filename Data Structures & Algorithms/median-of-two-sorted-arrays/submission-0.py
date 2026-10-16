class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2
        l1 = l2 = 0
        r1, r2 = len(nums1) - 1, len(nums2) - 1

        while True:
            m1 = (l1 + r1) // 2
            m2 = half - m1 - 2

            left1 = nums1[m1] if m1 >= 0 else float("-infinity")
            left2 = nums2[m2] if m2 >= 0 else float("-infinity")
            right1 = nums1[m1 + 1] if m1 < len(nums1) - 1 else float("infinity")
            right2 = nums2[m2 + 1] if m2 < len(nums2) - 1 else float("infinity")

            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r1 = m1 - 1
            else:
                l1 = m1 + 1


        

          