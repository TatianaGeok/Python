The merge_arrays(a, b) function, which is partly implemented below, 
takes two sorted lists of integers, 
merges them into one sorted list, 
and returns the result. 

The function should work in the following way: 
create an empty list c which will store the result; 
keep finding the smallest remaining element in a and b and moving it to the list c; 
stop when there are no elements left in a and b.

Note, that during the execution any of the lists a and b can become empty, 
so handle these cases carefully. 
Try to use non-boolean values in logical expressions when possible.

Your program shouldn't read any input or call the function, just implement it.

The expression in the while loop should check if there are any elements left in a or b.
The if statement should check if the next element should be taken from list a. 

This happens in two situations:
1) list b is empty;
2) both lists are not empty and the first element in a is less than the first element in b.

Sample Input 1:
1 2 3
2 3 4 4

Sample Output 1:
1 2 2 3 3 4 4
