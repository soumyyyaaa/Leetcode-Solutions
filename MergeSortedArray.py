def merge(nums1, m, nums2, n):
    for i in range(m, len(nums1)):
        nums1[i] = nums2[i-m]
    nums1.sort()
    return nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))