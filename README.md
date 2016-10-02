# data-structures

## Implement a singly-linked list in Python:
  * push(val) will insert the value ‘val’ at the head of the list
  * pop() will pop the first value off the head of the list and return it.
  * size() will return the length of the list
  * search(val) will return the node containing ‘val’ in the list, if present, else None
  * remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list)
  * display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

## Implement a stack in in Python:

  * push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
  * pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception class.

## Implemented a Doubly Linked list in Python:

  * push(val) will insert the value ‘val’ at the head of the list append(val) will append the value ‘val’ at the tail of the list
  * pop() will pop the first value off the head of the list and return it.
  * shift() will remove the last value from the tail of the list and return it.
  * remove(val) will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.

## Implement a queue in Python:

  * enqueue(value): adds value to the queue
  * dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
  * peek(): returns the next value in the queue without dequeueing it. If the queue is empty, returns None
  * size(): return the size of the queue. Should return 0 if the queue is empty.

## Implement a deque in Python:

  * append(val): adds value to the end of the deque
  * appendleft(val): adds a value to the front of the deque
  * pop(): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
  * popleft(): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
  * peek(): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
  * peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)

## Implement a binary heap in Python:

 * push(): puts a new value into the heap, maintaining the heap property.
 * pop(): removes the “top” value in the heap, maintaining the heap property.


# Implement a priority queue in Python:

 * insert() inserts an item into the queue.
 * pop() removes the most important item from the queue.
 * peek(): returns the most important item without removing it from the queue.

# Implement a graph in Python:

##Implement a graph with weighted edges in Python:

* nodes(): return a list of all nodes in the graph
* edges(): return a list of all edges in the graph
* add_node(n): adds a new node ‘n’ to the graph
* add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added
* del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
* del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
* has_node(n): True if node ‘n’ is contained in the graph, False if not.
* neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
* adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g

##Implement a Graph Travers:
* g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
* g.breadth_first_traversal(start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.

###Appreciation: The current implementation is the 4th attempt and after the code review on Wednesday. I wrote the following pysudo code during class:

```
Some pseudo Code for traverse function:

add start node to the stack
initialize empty result list (this should be a set or dict to reduce search time)
while the stack is not empty:
	set curser to the top of stack and remove it, pop()
	if curser not in result:
    append curser to the result list
    for each neigbor in curser
		   add neighbor to the stack
return result
```

###program output
```
Run Depth First and Breadth First Traversal
100,000 times each on the following graph

        0
      /   \
     2      3
    / \    / \
   4   5  6   7

Depth First Traversal  : [1, 3, 7, 6, 2, 5, 4] Run time: 0:00:01.647541
Breadth First Traversal: [1, 3, 7, 6, 2, 5, 4] Run time: 0:00:03.371413
```


## Shortest path
* not dijkstra's algorithem is not currently working


## Binary Search Tree (BST)
* size: Return the number of nodes in the BST
* insert(val): Insert a node with the value of val into the BST
* contains(val): Return True if there exists a node with the value of val in the BST.  Return False if the value is not pressent.
* depth(): Return the number of levels at the deepest part of the graph.
* balance(): Returns the difference in the depth of the left side of the graph and the right side of the graph. If the right side of the graph is deeper, this will return a negative number.

* Nodes also have a get_dot method that will output DOT language.
* This DOT notation can be printed, then in the command line redirected to a file. 
* From the command line run: dot -Tpng InputFile.dot -o OutputFile.png to create a visual graph.

For testing of the BST we created verious trees with random numbers.  One tree had 20 nodes with 
values from -100 to 100.  The list that was created was:
[-14, -43, 48, -10, -98, 94, -71, 35, 75, 73, -64, -35, -14, -87, -81, 90, -41, -68, -28]
which looks like:

![Binary Search Tree](/src/5.png)

Additionally we were asked to create best a worst case senarios for the search trees.  
Best case senario:

![Best case Binary Search Tree](/src/best.png)

Worst case senario:

![Worst case Binary Search Tree](/src/worst.png)



##Sort Methods
###Insertion Sort
Implemented 
###Merge Sort
Implemented
###Quick Sort
The Quick Sort is a portion sort strategy.  First, pick a pivot item.  
In our implementation of the Quick Sort this is the last item of the list.  
Then iterate through the list moving all items less then the pivot value
to one side of the array and all items greater than the pivot value to
the other side.  Then recursively Quick Sort the two halves of the list,
until there is one item in the sub-lists.  

The time complexity of the average case scenario would be O(nlog(n)).  
The best case scenario is a list where the pivot number chosen, 
happens to be the median value of the range.  This would cause equal
dividing of the array.  The worse case scenario, would be a list that
just contains the same value at all of its values.  In this worse case
scenario the quick degrades into O(n^2)



##Dependencies
* PIP
* graphviz - for dot graphs
* Appreciation to https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
