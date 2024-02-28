1. Arrays are fixed size compared to linked lists which are dynamically sized, therefore linked lists allow insertion, deletion and updates to its capacity such as the growth and shrink if the memory space is available
Arrays have indexes while linked lists do not, therefore arrays can be accessed if given certain index and linked lists have to be traveresed to find the element needed

2. A replace function can be implemented so it can minimize the impact of each standalone tasks because there are less operations you need to do, such as inserting, deleting, and possibly shifting the entire array and its elements around

3. Insertion sort - feasbile to implement a doubly linked list because it can insert elements easily by traversing the doubly linked list through nodes then comparing the adjecent nodes from the front or back of the list.

Merge sort - feasbile to implement a doubly linked list because merge sort is a divide and conquer alghoritim, so it breaks down the list into smaller subsets. However, unlike an array with its index, you would have to traverse through to find the smallest in the subarrays then merge and relink nodes them back into the sorted doubly linked list

4. Time complexity should stay the fairly consistent, with insertion sort in both cases being O(n) for best case and O(n^2) in average and worst cases. In merge sort, O(nlog(n)) in all cases. However, space complexity and possibly its performance between a doubly linked list and regular array is different based on how the techniques are implemented as linked lists and arrays differ. In general, linked lists are non-contingous and arrays are contingous which affect the memory allocation also linked lists uses node to traverse to an element while array elements have indexs.


