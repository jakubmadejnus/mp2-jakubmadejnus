"""
Problem: Sort an Array

Given an array of integers `nums`, sort the array in ascending order and return it. 
You must solve the problem without using any built-in sorting functions, achieving O(nlog(n)) time complexity and the smallest space complexity possible.

Example:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.

## successful implementation below:

def sortArray(nums):

    def mergeSort(nums):
        if len(nums) > 1:
    
            # Finding the mid of the array
            mid = len(nums)//2
    
            # Dividing the array elements
            L = nums[:mid]
    
            # Into 2 halves
            R = nums[mid:]
    
            # Sorting the first half
            mergeSort(L)
    
            # Sorting the second half
            mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
    
    mergeSort(nums)

    return nums

"""

def sortArray(nums):

    def heapify(nums, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is greater than root
        if l < N and nums[largest] < nums[l]:
            largest = l
    
        # See if right child of root exists and is greater than root
        if r < N and nums[largest] < nums[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]  # swap
    
            # Heapify the root.
            heapify(nums, N, largest)

    def heapSort(nums):
        N = len(nums)
 
        # Build a maxheap.
        for i in range(N//2 - 1, -1, -1):
            heapify(nums, N, i)
    
        # One by one extract elements
        for i in range(N-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # swap
            heapify(nums, i, 0)
    
    heapSort(nums)

    return nums
    

 
# The main function to sort an array of given size