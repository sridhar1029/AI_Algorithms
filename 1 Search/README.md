# Search Algorithms

In this part of the course you will learn about different types of 
search algorithms, and will see their implementation in python. 

Given a model of the world, and the possible action space we can take, 
the search algorithm is used to find a path to the goal state. The model 
of the world includes every last detail of the environment. We take a 
subset of that to search over for computational efficiency. We only keep 
the information that is required for the search. A Search State keeps 
only the details needed for planning. The more simplified your search 
problem is, the easier is it to search over it, but there is a risk of 
over simplification when the search would not be good enough.

A **Search State** can simply be thought of as an abstraction of the 
world. It keeps just the data required for the search.

## A Search State consists of -
- State space
- Start state
- Successor Function
- A goal test

The solution to a search problem is a sequence of actions(a Plan) 
which transforms the start state to the goal state.

Search operate over a model of the world -
- The agent does not actually try all the plans out in the real world. Planning 
is all done in Simulation.
- Your search is only as good as your model of the world.

So, selecting a good abstraction of the world to search over is very important.

## State Space Graph
It is a mathematical representation of a search problem. In a search 
graph each node(state) only occurs once. We can rarely build this full 
graph in memory, but it is a useful idea. We usually build on demand 
to save computation.

## Search Tree
This can be thought of as an expanded version of a State space Graph. 
Start state is the root node and the children are the successors. Nodes 
show states but actually correspond plans that achieve those states. 
There are a lot of repeated structure in a search tree. When you have 
cycles in a State Space Graph the corresponding search tree can be 
infinite. But still this is a very useful idea for search.

## Tree Search
- Expand potential plans.
- Maintain a Fringe of partial plans under consideration.
- Try to expand as few tree nodes as possible

##### Some of the important terms to look into -
- Fringe
- Expansion
- Exploration Strategy

A Fringe can be thought of as a priority queue kind of data structure 
that stores all the nodes that could be expanded next. Each search 
algorithm has a different way of selecting the next node(strategy) to expand from 
the fringe and rest of the algorithm remains the same. We will try to 
find the goal state with least expansion of tree nodes.

#### General Tree search algorithm
This is a basic prototype of how a general tree search algorithm works.
```html
function Tree_Search(problem, Strategy) {returns a solution or failure}
    initialize search tree using initial state of problem
    loop do:
        if there are no candidates for expansion then return failure
        else choose a  leaf node for expansion according to the stratergy
        
        if the node contains goal state then return the corresponding solution
        else expand the node and add all the resulting nodes to the search tree
    end
```

Search algorithms can be categorized into two main types - 
- Uninformed Search
- Informed Search

## Uninformed Search
This is the kind of search when we do not know anything about the goal state or 
we do not make any assumptions about where the goal state could be and we search 
in every possible direction for the goal state. These algorithms waste a lot of time 
searching in the wrong direction but this is a good way to start with learning 
search algorithms. So lets get started with the search algorithms.
 
#### Depth First Search
As the name suggests, the expansion strategy of this algorithm is depth first. 
Depth is given higher priority. The tree nodes deeper are selected from the fringe
to be expanded first and if two nodes have the same depth the one that came in 
first will be given higher priority. It may seem a little complicated now but once 
you go through the code and implement it yourself, you will get a clear idea of 
how it works. This algorithm is not guaranteed to find an optimal solution.

Some implementation details - 
- Strategy : Expand deepest node first.
- Implementing : Fringe is a STACK. As a stack follows LIFO(Last in First out) 
strategy, it is prefect for this algorithm.

#### Breadth First Search
This algorithm gives breadth higher priority. The shallower nodes are expanded 
first. The shallow first strategy helps this algorithm find the optimal solution, 
but it can take up a lot of space in memory as the fringe can be really large for 
this in the worst case. 

Some implementation details - 
- Strategy : Expand the shallowest node first.
- Implementing : Fringe is a QUEUE. As a Queue follows FIFO(First in First out) 
strategy, it is prefect for this algorithm.

#### Uniform-Cost Search
When each of the state transitions or paths have different weights the Uniform cost 
search is a really useful algorithm to use. This algorithms expansion strategy is 
to expand the cheapest node first. We use a priority queue in this case where the 
priority is given by the cost of the path. The cheapest node on the fringe is the 
one that is expanded first.

Some implementation details - 
- Strategy : Expand the cheapest node first.
- Implementing : Fringe is a PRIORITY QUEUE. Where priority is given by the cost 
of the path to that node.


## Informed Search
