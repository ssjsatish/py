'''
This is not a binary tree programming problem in the ordinary sense -- 
it's more of a math/combinatorics recursion problem that happens to use binary trees. 
Suppose you are building an N node binary search tree with the values 1..N. 
How many structurally different  binary search trees are there that store those values? 
Write a recursive function that, given the number of distinct values, 
computes the number of structurally unique binary search trees that store those values. 
For example, countTrees(4) should return 14, since there are 14  structurally unique binary search trees that store 1, 2, 3, and 4. 
The base case is easy, and the recursion is short but dense. Your code should not construct any actual trees; 
it's just a counting problem.
'''