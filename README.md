# data-structures

Implement a singly-linked list in Python:
  * push(val) will insert the value ‘val’ at the head of the list
  * pop() will pop the first value off the head of the list and return it.
  * size() will return the length of the list
  * search(val) will return the node containing ‘val’ in the list, if present, else None
  * remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list)
  * display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

Implement a stack in in Python:

  * push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
  * pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception class.

Implemented a Doubly Linked list in Python:

  * push(val) will insert the value ‘val’ at the head of the list append(val) will append the value ‘val’ at the tail of the list
  * pop() will pop the first value off the head of the list and return it.
  * shift() will remove the last value from the tail of the list and return it.
  * remove(val) will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.

Implement a queue in Python:

  * enqueue(value): adds value to the queue
  * dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
  * peek(): returns the next value in the queue without dequeueing it. If the queue is empty, returns None
  * size(): return the size of the queue. Should return 0 if the queue is empty.

Implement a deque in Python:

  * append(val): adds value to the end of the deque
  * appendleft(val): adds a value to the front of the deque
  * pop(): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
  * popleft(): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
  * peek(): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
  * peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)

Implement a binary heap in Python:

 * push(): puts a new value into the heap, maintaining the heap property.
 * pop(): removes the “top” value in the heap, maintaining the heap property.

 Implement a graph in Python:

* nodes(): return a list of all nodes in the graph
* edges(): return a list of all edges in the graph
* add_node(n): adds a new node ‘n’ to the graph
* add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
* del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
* del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
* has_node(n): True if node ‘n’ is contained in the graph, False if not.
* neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
* adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g

##Implement a Graph Travers:
* g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
* g.breadth_first_traversal(start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.

####Appreciation: The current implementation is the 4th attempt and after the code review on Wednesday. I wrote the following pysudo code during class:

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
Run Depth First and Breadth First Traversal
100,000 times each on the following graph

        0
      /   \
     2      3
    / \    / \
   4   5  6   7

Depth First Traversal  : [1, 3, 7, 6, 2, 5, 4] Run time: 0:00:01.647541
Breadth First Traversal: [1, 3, 7, 6, 2, 5, 4] Run time: 0:00:03.371413



Dependencies
# PIP

Appreciation to https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
