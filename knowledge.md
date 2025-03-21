# In General

-   If in question you have been given relation between two indices like `nums[j] - nums[i] != j -1` is a bad pairs so try to make it simple and move like terms with each other `nums[j] - j != nums[i] - i` this can make your problem simple and approachable. See LC 2364.

-   When ever you want to minimize the maximum or maximize the minimum then use binary search. see LC: 2560

# sliding window

-   Whenever question states about continuous subarray think if sliding window can be used or not using any type of prefix hashmap algo.

# Subsets

-   There can be `2^n` subsets we can create from a given n length array.

# Binary

## what is a set bit?

A set bit is a bit in a binary number that has a value of 1

## How to select bit range ?

In practical terms, for numbers constrained to be less than or equal to 10^7 (requiring a maximum of 24 bits), we only need to check bit positions 0 to 23 when working with 32-bit integers. For larger numbers, like those up to 10^9, we would check up to 30 bits, since 2^30 =1,073,741,824.n

## Count no of set bits / count no of 1's in a binary representation.

-   brian kernighan’s algorithm

## Create a binary of all 1's given a number

-   We left shift 1 with the length of the binary num and negating 1 from it will give us that last all ones before becoming the 1000...
    as left shift will create the binary nums staring with a single one and rest all zeros.

```py
num = 5
length = num.bit_length()
all_ones = (1 << length) - 1

# 5 -> 101
# length = 3
# (b0001 << 3) - 1 = (b1000) - 1= 8 - 1 = 7 => b111
```

## Odd or even ?

-   if the least significant digit is 1 then number is odd else even.
-   Eg 1. Bin(2) = b"10" least significant digit is 0 so its even.
-   Eg 2. Bin(3) = b"11" least significant digit is 1 so its odd.
-   odd & 1 => 1; even & 1 => 0

## Divide by 2 (using >> )

-   Diving any number by 2 can be done using right shift `>>` operator or chopping of the least significant digit from binary representation.
-   For even number division:
    -   Eg. Bin(100) = "0b1100100"; bin(50) = '0b110010'. This example shows that how right shift divides.
-   For odd num division
    -   Eg. bin(99) = '0b1100011'; bin(49) = '0b110001'. The int value of 99 / 2 will be used given since right shift will give the (num // 2) or the floor value of num / 2.

# Numbers

## How many digits in a number

-   Approx if we need to find out the approx digits in number then we can take log10(n). See lc 2698 for question reference.

## Powers of 2

-   All the numbers which are powers of 2 when divided by 2 will give even numbers.
-   Its not necessarily the case that dividing every even number by 2 will provide an even num.
-   Diving every odd number by 2 will give odd number.

# Heap

-   If asked about kth smallest take max heap and vice versa because heap can pop the top elements and if we take an example of kth smallest then max heap will have larger elements on the top and we can easily pop bigger elements. The size of the heap will be k. If a new element is added to the heap and its length gets greater than k then we will pop the largest (top element) and at the end out heap will have the smallest element at the top.

# DSU

-   used for dynamic graphs which are constantly changing.
-   Takes O(1) constant time to find if a node is connected with another given node.
-   It has 2 things:
    -   `find_parent()`: finds the parent of the node.
    -   `union`: has `rank` and `size`.

## Pseudo code:

1. find ultimate parent of u & v which is pu & pv.
2. Find rank of pu & pv.
3. Connect smaller rank to larger rank always.

-   **path compression**:
    -   Make the ultimate parent of all nodes as their parent.
    -   Eg.- 1 -> 2 -> 3 -> 4 -> 5. The parent of 5 should be 1 (ultimate parent) and not 4 as we want to get the parent in O(1) constant time to know whether two nodes are in the same component or not.

# String

## KMP String matching

-   Find the LSP Longest suffix prefix.
-   LSP[0] = 0 (since the first char will be only suffix and prefix).
-   After that we need to have a counter for prevLSP which is the previous LSP we have. Consider a string "AAACAAAA"

# Maths

## Handling -ve remainders

-   (num % k + k) % k

# sequence

## TC: 2^n \* n

-   `2^n`: Since at every recursion call we are taking elements till n starting from i. So 2 ^ n like in subsets where we take two possibilities at a time copy or not copy.
-   `n` : It is for the copy operation.

# Matrix

## 2D -> 1D array

-   if you want to change the array from 2d to 1d then use the following formula:
    `i * no_of_cols + j`
-   Why it works ?

i starts from 0 so it's help in getting the row number, + j means add in which column the element is present

for every i = 0, our answer would be simply j

Now suppose i = 1 that means we have to add all the previous column element which is n

If i = 2 that means we have to add 2 times previous column elements which is n\*2

Hence n \* i + j is the formula

# Graphs

## Graph Facts

-   This is what is think but if you want to convert an unidrected graph to a directed graph then do not consider the edge u -> v where u > v then we are just considering the edge again.

## Graph terminologies

-   Bridge in a graph: If a connection is broken and it broke the graph into two or more components is called a bridge in a graph.
-   SCC (Strongly connected components): where any node can be visited by every other node even if one link is broken.

## Topological sort

### Key Properties:

-   Only applicable to DAGs (Directed Acyclic Graphs).
-   There can be multiple valid topological orderings for a given DAG.
-   Used in scenarios where tasks have dependencies, like scheduling, course prerequisites, and build systems.

### How to Find Topological Order?

Two common approaches:

#### Kahn’s Algorithm (BFS-based)

-   Find all nodes with in-degree = 0 (no dependencies).
-   Remove them from the graph and reduce in-degrees of neighbors.
-   Repeat until all nodes are processed.
-   If there’s a cycle, the algorithm detects it.

#### DFS-based Approach

-   Perform DFS and push nodes to a stack after processing all descendants.
-   Pop from the stack to get the topological order.

### Time Complexity:

Both algorithms run in O(V+E), where V is the number of vertices and E is the number of edges.

### Cyclic graph using topo sort ?

topological sort is not possible for cyclic graphs because a topological sort requires a Directed Acyclic Graph (DAG). If a graph contains a cycle, at least one node will always have an unresolved dependency, preventing a valid linear ordering.

#### Why Not in Cyclic Graphs?

In a cycle, there exists a sequence of nodes where each node depends on the next one, eventually leading back to the starting node.
This creates a deadlock, making it impossible to determine a valid order.

#### How to Detect Cycles Before Sorting?

Kahn’s Algorithm (BFS): If the algorithm processes fewer nodes than the total count (V), a cycle exists.
DFS Approach: If a node is visited while it’s still in the recursion stack, a cycle is detected.

## Dijkstra Algo

-   Shortest algo from given start node to all other nodes.
-   Use min heap to get the shortest path from starting node.
-   Why do we use min heap ?
    Because in our heap we add (distance i, node i). And to reach node i we may have different paths consisting of various distances. So our min heap could have same node but with different distance: [(d1, n1), (d2, n1)] and we need the shortest distance, hence we use min heap.

-   Why do we not use simple queue ?
    It will still work but the Time and space complexity will increase gradually. Suppose from point a to b we have multiple distances, so it will be super optimize if we add the smallest dist first so that when larger dist come they will straight away gets discarded. But if the larger distances comes first we will add them to the queue and explore their paths/neighbors and extra pop and insert will be done for queue.
-   Cons
    -   Cant work with -ve edges.
    -   obviously cant work with -ve cycles. Neg cycles are those whose distances sum comes out be in -ve.

## Bellman-Ford Algo

-   Same as dijkstra but also works for -ve edges.
-   find the shortest path from given start node to all other nodes even in -ve path edges also.
-   only directed graphs.
-   Works best for sparse graphs/less connections between different vertices.
-   If undirected graph is given then convert it to directed but wont work for -ve edges. take an example of edges (a, b, -1) and (b, a, -1) they are forming -ve cycle.
-   Find shortest path in -ve path directed graphs as well !

### How Algo works ?

    - Iterates V-1 times, relaxing all edges in each iteration.
    - A final iteration detects negative weight cycles.

### How It Works on Undirected Graphs

-   In an undirected graph, each edge (u,v,w) implies that there is also an edge (v,u,w).
-   If there are only positive or zero-weight edges, Bellman-Ford runs as expected.
-   If negative weights are present, the algorithm might fail or incorrectly detect negative cycles where none exist.

### Challenges with Undirected Graphs

1. Double Relaxation Issue

-   Since every edge (u,v,w) is bidirectional, both u→v and v→u are relaxed separately.
-   This increases the number of relaxations and could cause unnecessary updates.

2. False Negative Cycle Detection

-   If an undirected graph contains a negative weight edge (e.g., (u,v,−5)), a cycle is automatically formed:
    -   u→v with weight -5
    -   v→u with weight -5
    -   The total cycle weight = -10, leading Bellman-Ford to incorrectly detect a negative weight cycle.
    -   However, this is not a real cycle in the sense of traversal—it’s just the nature of an undirected edge.

## Floyd Warshall

-   Goal is same as dijkstra and bellman but used to find distance from each node to every other node.

### What is the Floyd-Warshall Algorithm?

-   Easiest way to find out distance of each node from all other nodes.
-   The Floyd-Warshall algorithm is a dynamic programming approach used to find the shortest paths between all pairs of vertices in a weighted graph.

-   Works for both directed and undirected graphs (as long as they have no negative cycles).
-   Time Complexity: O(V^3)
-   Space Complexity: O(V^2) (for storing distances)

### ✅ When to use Floyd-Warshall?

When we need the shortest path between every pair of vertices.
When the graph is dense (many edges).
When we need a simple, iterative approach instead of running Dijkstra’s multiple times.

## Prim's algo

-   OBJECTIVE: To find Minimum spanning tree (MST).
-   Given the Graph (V, E) having V vertices/nodes and E edges we need to find out the minimum weight path edges that connects all the nodes with (v-1) edges.
-   Some questions ask only the minimum sum which the mst have and some question also ask about the path we build. To solve the path problem we take a parent vector to return the parent of each node which makes our mst.

### Code walkthrough

-   Here unlike dijkstra we first check visit status in the while loop after getting the top min element from the heap and then visits its neighbors no matter if they are already visited or not since in while loop we are taking care of the visited status and unlike dij we are not maintaining any distance vector so all the child/neigh will be added.

## Kruskal's algo

-   Objective is same as prims algo.
-   OBJECTIVE: To find Minimum spanning tree (MST).

### code walkthrough

-   Create an edges list (w, u, v) and sort it in ascending order.
-   Iterate over the edges list and check if current u and v are connected or not. If not connected then add take the union of both using `dsu` else continue.
-   At the end we will have our MST.

## Kosaraju Algo

-   Find the strongly connected components.
-   Works in DAG.

### Code walkthrough

-   Find the topological sort order.
-   Reverse all the edges.
-   Start the dfs again in reverse graph and check how many times we need to start dfs. The total counts of dfs run is the connected edges.

## Tarjan's algo

-   Helps to find the bridge in graph.

## Code walkthrough

-   Start the DfS and assign each node its time of insertion and lowest time.
-   Initially the insertion time and lowest time will both be same. The insertion time is just the time t at which node has been visited.
-   The low will be updated from the neighbors of the node. If a cycle is there then a previously visited node with lesser time of insertion can update its parent low time (since time of insertion will not be changed for parent as well as neig).
-   The only thing which is prohibited is that we cannot take low time from any node's parent and only from its other child/neighbors.
