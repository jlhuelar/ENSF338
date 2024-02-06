1.  The algorithm you will use to find the room would most likely be linear. Given just the information on the sign, you would pass each room individually until you found the correct room. This is a linear algorithm because you are passing by each room until you find the room you are looking for. This is like iterating through an array linearly by iterating each element in the array until you find the one you are looking for.

2.  Each room can be defined as a step in this case. Given this condition, it would take 15 steps to find the correct room starting from the signs.

3.  It is neither scenario. If following the signs, it would be near the end, but not the last room. It is also not the first room.

4.  Given this room layout, the best-case scenario would be finding the room on the first try and the worst-case scenario would be finding the room last.

5.  You would improve the algorithm by ignoring the signs. By memorizing the floor layout, you would recognize that the shortest path to the room would be by going right instead of left at the signs. It would then be the 6th room instead of the 15th room by taking this path instead.