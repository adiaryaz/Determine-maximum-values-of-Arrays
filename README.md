# Determine maximum values of Arrays

A program to compare two 1-dimensional arrays (lists) of integers, find the maximum value within each, and then determine the overall maximum value between them.

## 📝 Description

This program takes two separate lists of numbers as input. It must first validate that both lists contain *only* integers. If they do, it finds the maximum value from the first list and the maximum value from the second list. Finally, it compares these two maximums and outputs the one that is larger.

-----

## 🎯 Problem Statement

### Input:

  * Input 1: A list of numbers (`arr1`).
  * Input 2: A second list of numbers (`arr2`).

### Output:

  * The single highest integer value found across both lists.
  * "Cant determine, there are List" if *either* list contains a non-integer element.

### Rules:

1.  The program must read two separate lists.
2.  **Validation:** The program must check *both* lists. If *either* list contains any element that is not an integer (e.g., a string), it must output the error message "Cant determine, there are List".
3.  **Function Implementation:** A function must be used to find the maximum value of a single list.
4.  **Comparison:** The program must find the maximum of the first list (`max1`), find the maximum of the second list (`max2`), and then compare `max1` and `max2` to find the absolute maximum.

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[10, 2, 4, 10]
[2, 4, 10, 30, 2]
```

**Output:**

```
30
```

**Explanation:** The max of the first list is 10. The max of the second list is 30. The overall max is 30.

### Example 2 (Sample 2)

**Input:**

```
[1, 8, 2, 10, 18, 10, 15, 16]
[8, 10, 12, 20]
```

**Output:**

```
20
```

**Explanation:** The max of the first list is 18. The max of the second list is 20. The overall max is 20.

### Example 3 (Sample 6)

**Input:**

```
[10, "a", 19]
[19, 29, 19]
```

**Output:**

```
Cant determine, there are List
```

**Explanation:** The first list contains a non-integer (a string "a").

### Example 4 (Sample 7)

**Input:**

```
[10, 20, 30]
["a", 10, 30]
```

**Output:**

```
Cant determine, there are List
```

**Explanation:** The second list contains a non-integer (a string "a").

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/array-max-compare.git
    cd array-max-compare
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Enter the two arrays in list format (e.g., `[1, 4, 5]`) on separate lines when prompted to see the result.
