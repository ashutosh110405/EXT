class Solution:

    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        # Ensure nums1 is the smaller array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2  # Partition index for nums1
            j = half_len - i  # Partition index for nums2

            # Boundaries of partitions
            # If i = 0, max_left1 is -infinity (nothing on the left)
            # If i = m, min_right1 is +infinity (nothing on the right)
            max_left1 = float("-inf") if i == 0 else nums1[i - 1]
            min_right1 = float("inf") if i == m else nums1[i]

            max_left2 = float("-inf") if j == 0 else nums2[j - 1]
            min_right2 = float("inf") if j == n else nums2[j]

            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # If total length is even
                return (
                    max(max_left1, max_left2) + min(min_right1, min_right2)
                ) / 2.0

            elif max_left1 > min_right2:
                # i is too large, move to the left
                high = i - 1
            else:
                # i is too small, move to the right
                low = i + 1

        raise ValueError("Input arrays are not sorted or invalid.")