Add your answers to the Algorithms exercises here.
Exercise 1
a - Linear
b - O(log n)
c - O(sqroot(n))
d - O(n log n)
e - O(n ^ 3)
f - O(bunnies)
g - O(n)

Exercise 2
a - 
minimum = a[0]
difference = 0
for i in range (1, len(a)):
    minimum = min(minimum, a[i])
    difference = max(difference, a[i] - minimum)
return difference    
b - Binary Search

Exercise 3
a - first item = pivot
O n ^ 2
n pivots, n elements
b - O (n log n)
