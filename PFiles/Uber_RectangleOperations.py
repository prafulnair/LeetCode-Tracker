"""
### Problem: Rectangle Operations 

You are given an array `operations` where each element is an operation of one of the following two types:

1. `[0, a, b]` - Create and save a rectangle of size `a x b`.
2. `[1, a, b]` - Check if a rectangle of size `a x b` can fit inside all previously saved rectangles. You can rotate the rectangle `a x b` to be `b x a`.

The task is to return a list of booleans representing the answers to the second type of operation. If the rectangle can fit inside all previously saved rectangles, return `True`, otherwise return `False`. You can assume that a rectangle of size `a x b` can fit inside another rectangle of size `p x q` if either:
- `a <= p` and `b <= q`, or
- `b <= p` and `a <= q`.

### Constraints:
- `1 <= operations.length <= 10^5`
- Each operation has exactly 3 elements: `operations[i][0]` is either `0` or `1`, and `operations[i][1]` and `operations[i][2]` are positive integers representing the dimensions `a` and `b`.
- The rectangle dimensions `a` and `b` are positive integers, where `1 <= a, b <= 10^9`.

### Output:
Return an array of booleans. For each operation of type `[1, a, b]`, the result should be `True` if the rectangle can fit inside all saved rectangles, and `False` otherwise.

### Example 1:
```
Input: operations = [[1, 1, 1]]
Output: [True]
Explanation: There are no previously saved rectangles, so by default, the answer is True.
```

### Example 2:
```
Input: operations = [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1, 2, 4]]
Output: [True, False]
Explanation:
- After the first operation, we have a rectangle of size 3 x 3.
- After the second operation, we have a rectangle of size 5 x 2.
- For the third operation, we check if a 3 x 2 rectangle can fit inside both (either as 3x2 or 2x3), and it can, so the answer is True.
- For the fourth operation, we check if a 2 x 4 rectangle can fit inside the previously saved rectangles, and it cannot, so the answer is False.
```

### Example 3:
```
Input: operations = [[0, 6, 4], [0, 7, 3], [1, 5, 5]]
Output: [False]
Explanation:
- The largest rectangle we can save is 6x4 or 7x3.
- A rectangle of size 5x5 cannot fit inside any saved rectangle.
```

### Notes:
- The operations should proceed sequentially. When you process `operations[i]`, only the results of the previous operations `operations[0]` to `operations[i-1]` are available.
- For type `[1, a, b]`, you should check if the given rectangle (including its rotated form) fits in all saved rectangles from the previous operations of type `[0, a, b]`.
"""

# NOT PROPERLY SOLVED. 

def process_operations(operations):
    # Initialize the largest "container" rectangle
    max_width = 0
    max_height = 0
    result = []

    for operation in operations:
        if operation[0] == 0:
            # Create and save a rectangle of size a x b
            a, b = operation[1], operation[2]
            # Sort the dimensions so that the smaller one is always width and the larger one height
            width, height = min(a, b), max(a, b)
            # Update the maximum dimensions that can hold any other rectangle
            max_width = max(max_width, width)
            max_height = max(max_height, height)
        else:
            # Check if a rectangle of size a x b can fit inside all saved rectangles
            a, b = operation[1], operation[2]
            # Check if a x b (or b x a) fits in the max_width x max_height
            if (min(a, b) <= max_width and max(a, b) <= max_height):
                result.append(True)
            else:
                result.append(False)

    return result


operations = [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1, 2, 4]]
print(process_operations(operations))
