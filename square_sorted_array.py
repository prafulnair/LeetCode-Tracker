"""
    Problem: Given a sorted array of integers (which can be negative), 
    the task is to return a new array where each element is the square of 
    the corresponding element in the input array. The new array should also be 
    sorted in non-decreasing order.

    Key Aspects of the Solution:
    - The input array is sorted in non-decreasing order but contains negative numbers.
    - Squaring negative numbers can make them larger than the positive numbers, 
      so simply squaring the elements and sorting will not work efficiently.

    Two-Pointer Technique:
    - To solve this problem efficiently without extra sorting, we use a two-pointer approach.
    - Pointers 'p' and 'q' are initialized at the start (leftmost) and end (rightmost) 
      of the array, respectively.
    - We compare the squares of the elements pointed to by 'p' (left) and 'q' (right).
    - The larger squared value is placed at the 'high_index' (which starts at the last index 
      of the `squares` array and moves backward).
    - Depending on which square is larger, we either increment the left pointer ('p') 
      or decrement the right pointer ('q').
    - After placing the larger square at `high_index`, we decrement `high_index`.

    Efficiency and Considerations:
    - This solution works in O(n) time complexity because we only make a single pass 
      through the array.
    - The space complexity is O(n) for storing the result.

    Tricks and Tips:
    - Remember that sorting the squares in one pass with the two-pointer method is more 
      efficient than squaring all elements first and then sorting them (O(n log n)).
    - Keep an eye on off-by-one errors when working with two pointers, especially when 
      comparing values and updating the pointers.
    - Double-check array indices when assigning values to ensure that values are placed 
      in the correct order (from largest to smallest, starting from the end).
    """

class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    # TODO: Write your code here

    p, q = 0, len(arr) - 1
    high_index = len(arr) - 1
    while (p <= q):
      squared_left = arr[p] * arr[p]
      squared_right = arr[q] * arr[q]
      if squared_left >= squared_right:
        squares[high_index] = squared_left
        p += 1
      else:
        squares[high_index] = squared_right
        q -= 1
      high_index -= 1

    return squares
"""
Problem Statement

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

Constraints:

    1 <= arr.length <= 104
    -104 <= arr[i] <= 104
    arr is sorted in non-decreasing order.

"""