1. Time complexity for reserve() could be O(n). First, the for loop has to iterate through the linked least once which is O(n). Then with each iteration, it has to access each element O(n). Other operations include pointer manipulations which take time but higheer

2. Changes made is that index is removed to implement another way  to work better with larger lists rather than accessing indexes which takes time.
O(n) --> O(n^2)