1.  a) "Midpoint" is set where the item is likely to occur, therefore faster search
    b) The interpolation search will start closer to the entry wanted to find, more efficient position to divide data to then search for entry

2.  If the data follows a different distribution other than a uniform distribution, it will result in inaccurate search due to interpolation search assumes the data is sorted. The performance of interpolation search in a different distrution will be greatly and negatively impacted.

3.  The part of the code that will be affected is the values of low, pos, and high because it can not be assumed in a non-uniform distribution that the data in the array is sorted. 

4. Linear search will be the only option if both binary and interpolation search fails when the array of data to be searched is unsorted and possibly is a small set of data. 

5. When the chunk of search space is relatively small and data is unsorted. Linear search will outperform both binary and interpolation search because it searches through the array from index 0 all the way to the end of the data array regardless if the data is sorted or unsorted. With this, depending the on the position of data wanted to be found, linear search is more efficient on smaller sets of data.

6. To improve and make binary and interpolation data work, the data should be sorted in an alghoritm that makes the data sorted. This will make the low, mid/pos, and high variables work to function correctly.